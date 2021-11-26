import base64
import json
import random
import re
import requests

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    def upload(self) -> str:
        with open(self.path, 'rb') as f:
            base64Img = base64.b64encode(f.read()).decode()
        r = requests.post(
            'https://imio.jd.com/uploadfile/file/post.do',
            data={
                's': base64Img,
            },
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'X-Forwarded-For': '.'.join(str(random.randint(0, 255)) for x in range(4)),
            }
        )
        r.raise_for_status()
        return json.loads(re.search(r'<body>(.+)</body>', r.text).group(1))['path'].replace('http://', 'https://')
