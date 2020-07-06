import os

from importlib import import_module
from uploader import AbstractUploader

class Uploader:
    @staticmethod
    def get(server: str, path: str) -> AbstractUploader:
        return import_module(f'uploader.{server}').Uploader(path)

    @staticmethod
    def server() -> list:
        server_list = [os.path.splitext(x)[0] for x in os.listdir(os.path.dirname(__file__) + '/uploader') if os.path.splitext(x)[1].lower() == '.py']
        server_list.remove('__init__')
        return server_list
