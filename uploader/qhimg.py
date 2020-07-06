import json

from _abstract import AbstractUploader

class QhimgUploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://st.so.com/stu'

    @property
    def file_key(self) -> str:
        return 'upload'

    @property
    def form(self) -> dict:
        return {
            'src': 'st',
        }

    @property
    def parsed(self) -> str:
        query = self.request.headers['Location'].split('?')[1]
        query = {x[0]: x[1] for x in [x.split('=') for x in query.split('&')]}
        if not query['imgkey']:
            raise Exception()
        return f'https://ps.ssl.qhmsg.com/{query["imgkey"]}'
