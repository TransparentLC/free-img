import base64
import random
import requests
import secrets

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    def upload(self) -> str:
        with open(self.path, 'rb') as f:
            base64Img = base64.b64encode(f.read()).decode()
        r = requests.post(
            f'https://new-api.meiqia.com/upload?ent_id={secrets.token_urlsafe(6)}',
            files={
                'b64encoded': (None, base64Img),
            },
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'X-Forwarded-For': '.'.join(str(random.randint(0, 255)) for x in range(4)),
            }
        )
        r.raise_for_status()
        return r.json()['photo_url'].split('?')[0]
