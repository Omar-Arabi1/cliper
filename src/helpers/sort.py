from datetime import datetime
from . import clipboad_context

def sort(highest: bool = False, newest: bool = False, sort_by_priority: bool = False) -> dict:
    clipboard_content: dict = clipboad_context.read_json()
        
    if highest is True and sort_by_priority is True:
        clipboard_contents_by_priority: dict = dict(sorted(clipboard_content.items(), key=lambda copied_text: copied_text[1].get('priority'), reverse=True))
        return clipboard_contents_by_priority
    elif highest is False and sort_by_priority is True:
        clipboard_contents_by_priority: dict = dict(sorted(clipboard_content.items(), key=lambda copied_text: copied_text[1].get('priority')))
        return clipboard_contents_by_priority
    
    if newest is True and sort_by_priority is False:
        clipboard_contents_by_date: dict = dict(sorted(clipboard_content.items(), key=lambda test_date: datetime.strptime(test_date[1].get('creation_date'), '%Y-%m-%d'), reverse=True))
        return clipboard_contents_by_date
    elif newest is False and sort_by_priority is False:
        clipboard_contents_by_date: dict = dict(sorted(clipboard_content.items(), key=lambda test_date: datetime.strptime(test_date[1].get('creation_date'), '%Y-%m-%d')))
        return clipboard_contents_by_date
        