from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://mp.yidianzixun.com/upload?action=uploadimage'

    @property
    def file_key(self) -> str:
        return 'upfile'

    @property
    def parsed(self) -> str:
        return self.request.json()['url']
