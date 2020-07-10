import os
import requests

from abc import abstractmethod
from mimetypes import MimeTypes

class AbstractUploader:
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

    def upload(self) -> str:
        with open(self.path, 'rb') as f:
            r = requests.post(
                url=self.request_url,
                files={
                    self.file_key: (os.path.basename(f.name), f, MimeTypes().guess_type(f.name)[0]),
                },
                data=self.form,
                headers={
                    'User-Agent': 'curl/7.71.0',
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
