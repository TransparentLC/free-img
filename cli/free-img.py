#!/usr/bin/env python3

import argparse
import glob
import itertools
import os
import requests
import subprocess
import sys
import tempfile
import typing
from concurrent.futures import ThreadPoolExecutor

sys.path.append(os.path.realpath(os.path.dirname(__file__) + '/..'))

from __init__ import Uploader

s = requests.Session()

def upload(file: str, formatter: typing.Callable[[str, str], str], server: str, raw: bool, max_length: int):
    name = os.path.basename(file)
    temp = None

    try:
        if file.startswith('http://') or file.startswith('https://'):
            with open(temp := tempfile.mktemp(os.path.splitext(name)[1]), 'wb') as f:
                r = s.get(file, stream=True)
                for d in r.iter_content(None):
                    f.write(d)
            # match os.path.splitext(temp)[1]:
            #     case '.png':
            #         subprocess.run(('oxipng', '-o', 'max', '-v', '-v', temp)).check_returncode()
            #     case '.jpg':
            #         subprocess.run(('jpegtran-static', '-copy', 'none', '-optimize', '-progressive', '-outfile', temp, temp)).check_returncode()
        url = Uploader.get(server, temp or file).upload()
        result = formatter(url, name)
    except Exception as ex:
        result = f'\033[91m{type(ex).__name__}\033[39m \033[93m{ex}\033[39m'
    finally:
        if temp is not None and os.path.exists(temp):
            os.remove(temp)

    if not raw:
        result = f'\r{name.ljust(max_length)} -> \033[92m{result}\033[39m'
    print(result)

if __name__ == '__main__':
    result_formatter = {
        'plain': lambda url, name: url,
        'markdown': lambda url, name: f'![{name}]({url})',
        'html': lambda url, name: f'<img alt="{name}" src="{url}">',
        'bbcode': lambda url, name: f'[img]{url}[/img]',
    }

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        '--input',
        dest='input',
        type=str,
        nargs='+',
        required=True,
        help='The path of image(s) to upload.'
    )
    parser.add_argument(
        '-s',
        '--server',
        dest='server',
        type=str,
        choices=Uploader.server(),
        required=True,
        help='Upload throuth a given CDN server.'
    )
    parser.add_argument(
        '-f',
        '--format',
        dest='format',
        type=str,
        choices=result_formatter.keys(),
        default='plain',
        help='The format of uploaded URL.'
    )
    parser.add_argument(
        '-r',
        '--raw',
        dest='raw',
        action='store_true',
        help='Raw output.'
    )
    parser.add_argument(
        '-g',
        '--glob',
        dest='glob',
        action='store_true',
        help='Use glob on the image\'s path.'
    )
    parser.add_argument(
        '-m',
        '--multithread',
        dest='multithread',
        action='store_true',
        help='Enable multithreaded uploading. The output may be messed up!'
    )
    args = parser.parse_args()

    if args.glob:
        files = tuple(item for sublist in (glob.glob(x) for x in args.input) for item in sublist)
    else:
        files = args.input

    if not files:
        print('Nothing will be uploaded.')
        exit(1)

    max_length = max(len(os.path.basename(x)) for x in files)

    if args.multithread:
        try:
            with ThreadPoolExecutor(16) as executor:
                executor.map(
                    upload,
                    files,
                    itertools.repeat(result_formatter[args.format]),
                    itertools.repeat(args.server),
                    itertools.repeat(args.raw),
                    itertools.repeat(max_length),
                )
        except KeyboardInterrupt:
            exit(1)
    else:
        for i in files:
            upload(i, result_formatter[args.format], args.server, args.raw, max_length)
