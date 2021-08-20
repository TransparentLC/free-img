from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://bbs.ldmnq.com/api/bbs/upload?dir=topic/attachment'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def parsed(self) -> str:
        return self.request.json()['data']['data'][0]
