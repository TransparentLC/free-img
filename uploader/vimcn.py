from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://img.vim-cn.com/'

    @property
    def file_key(self) -> str:
        return 'image'

    @property
    def parsed(self) -> str:
        return self.request.text.strip()
