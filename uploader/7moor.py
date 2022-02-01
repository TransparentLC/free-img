import json
import random
import requests

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    def upload(self) -> str:
        upkey = f'im/2768a390-5474-11ea-afc9-7b323e3e16c0/{self.filename_rewrite(self.path)}'
        # upkey = f'im/ce3d5ef0-6836-11e6-85a2-2d5b0666fd02/{self.filename_rewrite(self.path)}'
        r = requests.get(
            f'https://ykf-webchat.7moor.com/chat?data={json.dumps({"action": "qiniu.getUptokenFromCustomer", "key": upkey})}',
            # f'https://webchat.7moor.com/chat?data={json.dumps({"action": "qiniu.getUptokenFromCustomer", "key": upkey})}',
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'X-Forwarded-For': '.'.join(str(random.randint(0, 255)) for x in range(4)),
            }
        )
        r.raise_for_status()
        resp = r.json()
        if not resp['success']:
            raise RuntimeError('Failed to upload')
        uptoken = resp['uptoken']

        with open(self.path, 'rb') as f:
            r = requests.post(
                'https://up.qbox.me/',
                files={
                    'file': f,
                },
                data={
                    'name': f.name,
                    'key': upkey,
                    'token': uptoken,
                },
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                    'X-Forwarded-For': '.'.join(str(random.randint(0, 255)) for x in range(4)),
                }
            )
            r.raise_for_status()
        return f'https://fs-im-kefu.7moor-fs2.com/{r.json()["key"]}'
