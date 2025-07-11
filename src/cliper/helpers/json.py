from json import dump, load
from os.path import exists
from os import mknod
import getpass

class Json():
    def __init__(self, json_file_path: str) -> None:
        self._json_file_path: str = json_file_path
    
    def create_data_file(self) -> None:
        if not exists(self._json_file_path):
            user: str = getpass.getuser()
            self._json_file_path = f'/home/{user}/.clipboard_contents.json'
            mknod(self._json_file_path)
            file = open(f'/home/{user}/.clipboard_contents.json', mode='w', encoding='utf-8')
            file.write('{}')
            file.close()
    
    def write_json(self, data_to_write: dict) -> None:
        with open(self._json_file_path, mode='w', encoding='utf-8') as write_file:
            dump(data_to_write, write_file, indent=4)
        
    def read_json(self) -> dict:
        with open(self._json_file_path, mode='r', encoding='utf-8') as read_file:
            return load(read_file)