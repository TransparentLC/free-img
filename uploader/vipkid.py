import hashlib
import mimetypes
import os
import random
import requests
import secrets
import time

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    def upload(self) -> str:
        h = {
            'appid': 'csc',
            'timestamp': time.strftime('%Y%m%d%H%M%S'),
            'nonce': secrets.token_urlsafe(24),
            'signature': '3c99a72b33e34f5fb71ccc98cd750096',
        }
        h['signature'] = hashlib.sha1(''.join(sorted(h.values())).encode()).hexdigest()
        with open(self.path, 'rb') as f:
            r = requests.post(
                'https://uc-im-framework.vipkid.com.cn/v/fw/vos/media/upload',
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                    'X-Forwarded-For': '.'.join(str(random.randint(0, 255)) for x in range(4)),
                    **h,
                },
                files={
                    'file': (self.filename_rewrite(os.path.basename(f.name)), f, mimetypes.guess_type(self.filename_rewrite(f.name))[0] or 'image/jpeg'),
                },
            )
        r.raise_for_status()
        return r.json()['data']['url']
