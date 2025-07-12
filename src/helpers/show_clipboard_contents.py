from tabulate import tabulate

def show_clipboard_contents(clipboard_contents: dict) -> None:
    """
    shows the clipboard's contents (creation_date, label, contents, priority)
    in a tabular format
    
    PARAMS: clipboard_contents: dict = the data that will be represented
    
    EXAMPLE:
        >>> show_clipboard_contents(clipboard_contents={'name': 'Mohamed'})
        output: name
                -----
                Mohamed
    
    NOTE: it won't exactly look like this just pass in the dictionary to show, and that dictionary must only be 
          the main data dictionary containing the json file's contents
    """
    headers: list[str] = ['creation date', 'label', 'contents', 'priority']
    contents: list[str] = list(clipboard_contents.keys())
    rows: list[list] = []

    for content in contents:
        data: dict = clipboard_contents.get(content)
        label: str = data.get('label')
        priority: str = str(data.get('priority'))
        creation_date: str = data.get('creation_date')
        rows.append([creation_date, label, content, priority])
    
    table: list[list] = [row for row in rows]
    
    print(tabulate(table, headers))