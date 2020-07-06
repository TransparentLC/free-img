import json

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://you.163.com/xhr/file/upload.json'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def form(self) -> dict:
        return {
            'format': 'json',
        }

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['data'][0].replace('http://', 'https://')
