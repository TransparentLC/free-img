import json
import random
import requests

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    def upload(self) -> str:
        upkey = f'im/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/{self.filename_rewrite(self.path)}'
        r = requests.get(
            f'https://webchat.7moor.com/chat?data={json.dumps({"action": "cos.getUptokenFromCustomer", "key": upkey})}',
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'X-Forwarded-For': '.'.join(str(random.randint(0, 255)) for x in range(4)),
            }
        )
        r.raise_for_status()
        resp = r.json()
        if not resp['success']:
            raise RuntimeError('Failed to upload')
        putUrl = resp['putUrl']

        with open(self.path, 'rb') as f:
            r = requests.put(
                putUrl,
                data=f,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                    'X-Forwarded-For': '.'.join(str(random.randint(0, 255)) for x in range(4)),
                }
            )
            r.raise_for_status()
        return f'https://cc-im-kefu-cos.7moor-fs1.com/{upkey}'
