# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 20:08:22 2022

@author: LocalAdmin
"""
import requests
import os


class YaUploader:
    HOST = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_status_code(self, file_path):
        url = self.HOST + 'v1/disk/resources'
        return requests.get(f'{url}?path={file_path}', headers=self._get_headers())

    def create_directory(self, file_path):
        url = self.HOST + 'v1/disk/resources'
        return requests.put(f'{url}?path={file_path}', headers=self._get_headers())

    def get_upload_link(self, file_path):
        url = self.HOST + 'v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': 'true'}
        return requests.get(url=url, headers=self._get_headers(), params=params).json()

    def upload(self, file_path: str, file_name):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_upload_link(file_path).get("href", "")
        resp = requests.put(href, data=open(file_name, 'rb'))
        resp.raise_for_status()
        return resp.status_code


def upload_list_files(token, path_to_file):
    uploader = YaUploader(token)
    uploader.create_directory(path_to_file)
    os.chdir(str(os.getcwd()).replace('\\', '/') + f'/{path_to_file}')
    file_list = os.listdir(addres_data)
    for i in file_list:
        result = uploader.upload(path_to_file + f'/{i}', i)
        if result == 201:
            print('Succes')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'upload_data'
    token = ''
    upload_list_files(token, path_to_file)
