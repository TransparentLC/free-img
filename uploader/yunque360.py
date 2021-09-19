import os
import random
import requests

from uploader import AbstractUploader
from urllib import parse

class Uploader(AbstractUploader):
    def upload(self) -> str:
        ext = os.path.splitext(self.path)[1][1:].lower()
        r = requests.post(
            'https://api.yunque360.com/v1/chat/im/uptoken',
            data=parse.urlencode({
                'ext': ext if ext in {'jpg', 'png', 'gif'} else 'jpg',
                'type': 'chat',
            }),
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'X-Forwarded-For': '.'.join(str(random.randint(0, 255)) for x in range(4)),
            }
        )
        r.raise_for_status()
        resp = r.json()
        if not resp['success']:
            raise RuntimeError('Failed to upload')
        resp = resp['data']

        accessId = resp['access_id']
        policy = resp['policy']
        signature = resp['signature']
        filename = resp['filename']
        host = resp['viewhost']

        with open(self.path, 'rb') as f:
            r = requests.post(
                'https://yunque-chat.oss-cn-hangzhou.aliyuncs.com/',
                files={
                    'file': f,
                },
                data={
                    'OSSAccessKeyId': accessId,
                    'policy': policy,
                    'Signature': signature,
                    'key': filename,
                },
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                    'X-Forwarded-For': '.'.join(str(random.randint(0, 255)) for x in range(4)),
                }
            )
            r.raise_for_status()
        return f'https:{host}/{filename}'
