from tabulate import tabulate

def show_clipboard_contents(clipboard_contents: dict) -> None:
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