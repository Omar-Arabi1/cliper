from datetime import datetime
from . import clipboad_context

def sort(highest: bool = False, newest: bool = False, sort_by_priority: bool = False) -> dict:
    """
    a function that sorts based on date or priority of the list when iterating through it to show
    to the user
    
    PARAMS: highest: bool = it determines wether or not the priorites will be sorted from highest to lowest or vise versa (only works for priority sorting)
    PARAMS: newest: bool = it determines wether or not the dates will be sorted from oldest to newest or vise versa (only works for date sorting)
    PARAMS: sort_by_priority: bool = it determines wether or not the you will sort the by priority or by date
    
    EXAMPLE:
        >>> sort(highest=True, newest=False, sort_by_priority=True)
        return -> clipboard_contents_sorted
    """
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
        