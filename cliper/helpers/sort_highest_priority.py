from . import clipboad_context

def sort_highest_priority() -> dict:
    clipboard_content: dict = clipboad_context.read_json()
    updated_clipboard_content: dict = {}
    priorities: list[int] = []
    
    for copied_text in clipboard_content:
        data: dict = clipboard_content.get(copied_text)
        priority: int = data.get('priority')
        priorities.append(priority)
    
    priorities.sort(reverse=True)
    
    for highest_priority in priorities:
        for copied_text in clipboard_content:
            data: dict = clipboard_content.get(copied_text)
            current_priority: int = data.get('priority')
            current_label: str = data.get('label')
            if current_priority == highest_priority:
                updated_clipboard_content.update({
                    copied_text: {
                        'priority': current_priority, 
                        'label': current_label
                    }
                })
                continue
    
    return updated_clipboard_content