import json
import random
import os
import string

from uploader import AbstractUploader

class Uploader(AbstractUploader):
    @property
    def request_url(self) -> str:
        return 'https://kf.dianping.com/api/file/burstUploadFile'

    @property
    def file_key(self) -> str:
        return 'files'

    @property
    def form(self) -> dict:
        return {
            'partSize': 1,
            'part': 0,
            'fileName': ''.join(random.choices(string.ascii_letters + string.digits, k=8)),
            'fileID': random.randint(0, 0xFFFFFFFF),
        }

    @property
    def parsed(self) -> str:
        return json.loads(self.request.text)['data']['uploadPath'].replace('http://', 'https://').replace('s3plus.meituan.net:80', 's3plus.meituan.net')

    @property
    def headers(self) -> dict:
        return {
            'CSC-VisitId': '',
        }

    def filename_rewrite(self, filename: str) -> str:
        if os.path.splitext(filename.lower())[1] in ('.webp', '.avif'):
            filename += '.jpg'
        return filename
