import json

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://api.open.oppomobile.com/api/utility/upload'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def form(self) -> dict:
        return {
            'type': 'feedback',
        }

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['data']['url']