from . import clipboad_context

def sort(highest: bool) -> dict:
    clipboard_content: dict = clipboad_context.read_json()
    
    if highest is True:
        clipboard_contents_by_priority: dict = dict(sorted(clipboard_content.items(), key=lambda user: user[1].get('priority'), reverse=True))
    else:
        clipboard_contents_by_priority: dict = dict(sorted(clipboard_content.items(), key=lambda user: user[1].get('priority')))
    return clipboard_contents_by_priority