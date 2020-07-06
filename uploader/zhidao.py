import json

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://zhidao.baidu.com/submit/ajax'

    @property
    def file_key(self) -> str:
        return 'image'

    @property
    def form(self) -> dict:
        return {
            'cm': 100672,
        }

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['url'].split('?')[0]
