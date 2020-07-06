import json

from _abstract import AbstractUploader

class MeituanUploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://chat.dianping.com/upload'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['path']
