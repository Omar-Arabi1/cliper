from json import load

def read_json() -> dict:
    path_to_json = '/home/omar-arabi/repos/cliper/clipboard_content.json'
    with open(path_to_json, mode='r', encoding='utf-8') as read_file:
        return load(read_file)