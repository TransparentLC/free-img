import os
import mimetypes
import random
import requests
import secrets

from abc import abstractmethod

mimetypes.add_type('image/avif', '.avif')

class AbstractUploader:
    path: str
    request: requests.Request

    def __init__(self, path: str) -> str:
        self.path = path
        self.request = None

    @property
    @abstractmethod
    def request_url(self) -> str:
        pass

    @property
    @abstractmethod
    def file_key(self) -> str:
        pass

    @property
    def form(self) -> dict:
        return {}

    @property
    def parsed(self) -> str:
        return self.request.text

    @property
    def headers(self) -> dict:
        return {}

    def filename_rewrite(self, filename: str) -> str:
        return secrets.token_urlsafe(6) + os.path.splitext(filename)[1]

    def upload(self) -> str:
        with open(self.path, 'rb') as f:
            r = requests.post(
                url=self.request_url,
                files={
                    self.file_key: (self.filename_rewrite(os.path.basename(f.name)), f, mimetypes.guess_type(self.filename_rewrite(f.name))[0] or 'image/jpeg'),
                },
                data=self.form,
                headers={
                    **{
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                        'X-Forwarded-For': '.'.join(str(random.randint(0, 255)) for x in range(4)),
                    },
                    **self.headers,
                },
                allow_redirects=False
            )
        r.encoding = 'utf-8'
        r.raise_for_status()
        self.request = r

        try:
            parsed = self.parsed
            if not parsed:
                raise RuntimeError('Failed to upload')
        except Exception as ex:
            # print(self.request.text)
            raise ex

        return parsed
