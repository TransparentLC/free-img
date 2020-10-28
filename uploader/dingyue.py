import json

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'http://upload.buzz.163.com/picupload'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def form(self) -> dict:
        return {
            'from': 'neteasecode_mp',
        }

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['data']['url'].replace('http://', 'https://')
