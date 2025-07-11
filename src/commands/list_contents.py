import click
from colorama import Fore
from tabulate import tabulate

from helpers import clipboad_context
from helpers.sort_highest_priority import sort_highest_priority
from helpers.check_clipboard_empty import check_if_empty

@click.command(help='list through all the saved copied texts you have')
@click.option('-shp', '--sort-by-heighest-priority', help='print the list sorted from highest priority rank', default=False, is_flag=True)
def list_contents(sort_by_heighest_priority: bool) -> None:
    check_if_empty()
    clipboard_contents: dict = clipboad_context.read_json()
    headers: list[str] = ['label', 'contents', 'priority']
    contents: list[str] = list(clipboard_contents.keys())
    row1: list[str] = []
    row2: list[str] = []
    row3: list[str] = []
    table: list[list] = [row1, row2, row3]

    for count, content in enumerate(contents):
        data: dict = clipboard_contents.get(content)
        label: str = data.get('label')
        priority: str = str(data.get('priority'))
        if count == 0:
            row1.extend([label, content, priority])
        elif count == 1:
            row2.extend([label, content, priority])
        elif count == 2:
            row3.extend([label, content, priority])
        
    print(tabulate(table, headers))
