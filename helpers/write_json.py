from json import dump

def write_json(data_to_write: dict) -> None:
    path_to_json = '/home/omar-arabi/repos/cliper/clipboard_content.json'
    with open(path_to_json, mode='w', encoding='utf-8') as write_file:
        dump(data_to_write, write_file, indent=4)