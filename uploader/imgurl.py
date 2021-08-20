from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://imgurl.org/upload/ftp'

    @property
    def file_key(self) -> str:
        return 'file'

    @property
    def parsed(self) -> str:
        return self.request.json()['url']
