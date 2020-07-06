import json

from _abstract import AbstractUploader

class MiUploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://shopapi.io.mi.com/homemanage/shop/uploadpic'

    @property
    def file_key(self) -> str:
        return 'pic'

    @property
    def parsed(self) -> str:
        url, query = json.loads(self.request.text)['result'].split('?')
        query = {x[0]: x[1] for x in [x.split('=') for x in query.split('&')]}
        if not query['id']:
            raise Exception()
        query = {'id': query['id']}
        return f'{url}?{"&".join(f"{k}={v}" for k, v in query.items())}'
