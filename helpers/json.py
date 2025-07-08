from json import dump, load

class Json():
    def __init__(self, json_file_path: str) -> None:
        self.json_file_path: str = json_file_path
    
    def write_json(self, data_to_write: dict) -> None:
        with open(self.json_file_path, mode='w', encoding='utf-8') as write_file:
            dump(data_to_write, write_file, indent=4)
        
    def read_json(self) -> dict:
        with open(self.json_file_path, mode='r', encoding='utf-8') as read_file:
            return load(read_file)