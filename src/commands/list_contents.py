from colorama import Fore
import click
from typing import Optional
import sys

from helpers import clipboad_context
from helpers.sort import sort
from helpers.check_clipboard_empty import check_if_empty
from helpers.show_clipboard_contents import show_clipboard_contents

@click.command(help='list through all the saved copied texts you have')
@click.option('-s', '--sort-by', help='print the table sorted starting from highest priority or lowest takes in highest/lowest', default=None)
def list_contents(sort_by: Optional[str]) -> None:
    check_if_empty()
    clipboard_contents: dict = clipboad_context.read_json()

    if sort_by is None:
        show_clipboard_contents(clipboard_contents=clipboard_contents)
        sys.exit()
    
    if sort_by.lower() == 'highest':
        clipboard_contents_sorted: dict = sort(highest=True)
    elif sort_by.lower() == 'lowest':
        clipboard_contents_sorted: dict = sort(highest=False)
    else:
        click.echo(Fore.RED + "Invalid option, you could put 'highest' or 'lowest' only")
        sys.exit()
    show_clipboard_contents(clipboard_contents=clipboard_contents_sorted)
