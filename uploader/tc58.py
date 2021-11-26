import base64
import json
import random
import requests

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    def upload(self) -> str:
        with open(self.path, 'rb') as f:
            base64Img = base64.b64encode(f.read()).decode()
        r = requests.post(
            'https://upload.58cdn.com.cn/json',
            data=json.dumps({
                'Pic-Size': '0*0',
                'Pic-Encoding': 'base64',
                'Pic-Path': '/nowater/webim/big/',
                'Pic-Data': base64Img,
            }),
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'X-Forwarded-For': '.'.join(str(random.randint(0, 255)) for x in range(4)),
                'Content-Type': 'application/json',
            }
        )
        r.raise_for_status()
        return f'https://pic{random.randint(1, 8)}.58cdn.com.cn/nowater/webim/big/{r.text}'
