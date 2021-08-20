from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://pic.sogou.com/pic/upload_pic.jsp'

    @property
    def file_key(self) -> str:
        return 'upload'

    @property
    def parsed(self) -> str:
        return self.request.text.replace('http://', 'https://')
