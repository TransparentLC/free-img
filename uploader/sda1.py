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
        r = s.get('https://p.sda1.dev/assets/css/thumb.css')

        filename = os.path.basename(self.path)
        if os.path.splitext(filename.lower())[1] not in {'.jpg', '.jpeg', '.gif', '.png', '.webp'}:
            filename += '.jpg'
        filename = self.filename_rewrite(filename)

        r = s.post(
            f'https://p.sda1.dev/api_dup{random.randint(0, 9)}/v1/upload_noform',
            params={
                'batch_size': 1,
                'filename': filename,
            },
            data=streamUpload(self.path),
        )
        resp = r.json()
        if not resp['success']:
            raise RuntimeError('Failed to upload')
        return resp['data']['url']
