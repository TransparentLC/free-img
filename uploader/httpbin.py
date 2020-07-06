import json

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://httpbin.org/post'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def form(self) -> dict:
        return {
            'key': 'value',
        }

    @property
    def parsed(self) -> str:
        # print('Hint: This upload server is used for test!')
        return json.loads(self.request.text)['url']
