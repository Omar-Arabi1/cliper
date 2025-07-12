from json import dump, load
from os.path import exists
from os import mknod
import getpass

class Json():
    """
    a json object for basic json functionality like writing the json file reading it
    or creating it if it doesn't exist yet in the desired location on disk
    """
    def __init__(self, json_file_path: str) -> None:
        """
        PARAMS: json_file_path: str = a path to the json file that will be used for writing/reading 
        """
        self._json_file_path: str = json_file_path

    def create_data_file(self) -> None:
        """
        checks if the desired json file exists at the desired location if not it creats it
        
        EXAMPLE:
            >>> json_helper.create_data_file()
        """
        if not exists(self._json_file_path):
            user: str = getpass.getuser()
            self._json_file_path = f'/home/{user}/.clipboard_contents.json'
            mknod(self._json_file_path)
            file = open(f'/home/{user}/.clipboard_contents.json', mode='w', encoding='utf-8')
            file.write('{}')
            file.close()

    def write_json(self, data_to_write: dict) -> None:
        """
        writes the json file to the desired file
        
        PARAMS: data_to_write: dict = the dictionary to serialize to write into the json file
        
        EXAMPLE:
            >>> json_helper.write_json(data_to_write={'name': 'Mohamed'})
        """
        with open(self._json_file_path, mode='w', encoding='utf-8') as write_file:
            dump(data_to_write, write_file, indent=4)

    def read_json(self) -> dict:
        """
        reads the json file and serialized it into a python dictionary
        
        EXAMPLE:
            >>> json_helper.read_json()
        """
        with open(self._json_file_path, mode='r', encoding='utf-8') as read_file:
            return load(read_file)
