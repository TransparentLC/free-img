import os
import random
import requests

from uploader import AbstractUploader

def streamUpload(path: str, chunk: int = 65536):
    with open(path, 'rb') as f:
        while data := f.read(chunk):
            yield data

class Uploader(AbstractUploader):
    def upload(self) -> str:
        s = requests.Session()
        s.hooks['response'].append(lambda r, *args, **kwargs: r.raise_for_status())

        filename = os.path.basename(self.path)
        if os.path.splitext(filename.lower())[1] not in {'.jpg', '.jpeg', '.gif', '.png', '.webp', '.svg'}:
            filename += '.jpg'
        filename = self.filename_rewrite(filename)

        r = s.post(
            'https://p.sda1.dev/api/v1/upload_external_noform',
            params={
                'filename': filename,
            },
            data=streamUpload(self.path),
        )
        resp = r.json()
        if not resp['success']:
            raise RuntimeError('Failed to upload')
        return os.path.split(resp['data']['url'])[0]
