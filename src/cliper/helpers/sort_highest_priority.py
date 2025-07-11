from . import clipboad_context

def sort_highest_priority() -> dict:
    clipboard_content: dict = clipboad_context.read_json()
    
    clipboard_contents_by_priority: dict = dict(sorted(clipboard_content.items(), key=lambda user: user[1].get('priority'), reverse=True))
    
    return clipboard_contents_by_priority