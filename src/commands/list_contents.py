import click
from colorama import Fore
from tabulate import tabulate

from helpers import clipboad_context
from helpers.sort_highest_priority import sort_highest_priority
from helpers.check_clipboard_empty import check_if_empty
from helpers.show_clipboard_contents import show_clipboard_contents

@click.command(help='list through all the saved copied texts you have')
@click.option('-shp', '--sort-by-heighest-priority', help='print the list sorted from highest priority rank', default=False, is_flag=True)
def list_contents(sort_by_heighest_priority: bool) -> None:
    check_if_empty()
    clipboard_contents: dict = clipboad_context.read_json()
    
    if sort_by_heighest_priority is False:
        show_clipboard_contents(clipboard_contents=clipboard_contents)
        return
    clipboard_contents_sorted: dict = sort_highest_priority()
    show_clipboard_contents(clipboard_contents=clipboard_contents_sorted)
