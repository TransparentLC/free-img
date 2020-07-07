#!/usr/bin/env python3

import argparse
import glob
import os
import sys

sys.path.append(os.path.realpath(os.path.dirname(__file__) + '/..'))

from __init__ import Uploader

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
    help='The path of image(s) to upload. Globbing is supported.'
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
args = parser.parse_args()

files = [glob.glob(x) for x in args.input]
files = [item for sublist in files for item in sublist]
max_length = max(map(lambda x: len(os.path.basename(x)), files))

for i in files:
    name = os.path.basename(i)
    formatter = result_formatter[args.format]

    if not args.raw:
        print(f'{name.ljust(max_length)} -> Uploading...', end='')

    try:
        url = Uploader.get(args.server, i).upload()
    except Exception as ex:
        # url = f'\033[91m{type(ex).__name__}\033[39m \033[93m{ex}\033[39m'
        url = '\033[91mFailed to upload\033[39m'
        formatter = result_formatter['plain']

    result = formatter(url, name)

    if not args.raw:
        print(f'\r{name.ljust(max_length)} -> \033[92m{result}\033[39m')
    else:
        print(result)
