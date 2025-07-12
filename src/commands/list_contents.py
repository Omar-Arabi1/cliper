from colorama import Fore
import click
from typing import Optional
import sys

from helpers import clipboad_context
from helpers.sort import sort
from helpers.check_clipboard_empty import check_if_empty
from helpers.show_clipboard_contents import show_clipboard_contents

@click.command(help='list through all the saved copied texts you have')
@click.option('-p', '--priority', help="it takes in highest/lowest to sort by priority", default=None)
@click.option('-d', '--date', help="it takes in oldest/newest to sort by date", default=None)
def list_contents(priority: Optional[str], date: Optional[str]) -> None:
    """
    use this command to list your clipboard it takes in an optional priority or date
    can't take both each of them has its own arguments
    
    priority: means sort by priority and takes in highest or lowest 
    date: means sort by date and takes in oldest or newest
    
    by default it lists them at the order that they are saved in inside the json file
    
    PARAMS: priority: Optional[str] = takes in highest or lowest to determine wether to list from highest or lowest (based on priority)
    PARAMS: date: Optional[str] = takes in an oldest or newest to show the list based on date
    
    EXAMPLE:
        >>> cliper list-contents -p highest
        output -> (can't show the output here its a bit difficult)
    """
    check_if_empty()
    clipboard_contents: dict = clipboad_context.read_json()

    if priority is None and date is None:
        show_clipboard_contents(clipboard_contents=clipboard_contents)
        sys.exit()

    if priority is not None:
        if priority.lower() == 'highest':
            clipboard_contents_sorted: dict = sort(highest=True, newest=False, sort_by_priority=True)
        elif priority.lower() == 'lowest':
            clipboard_contents_sorted: dict = sort(highest=False, newest=False, sort_by_priority=True)
        else:
            click.echo(Fore.RED + "Invalid option, you could put 'highest' or 'lowest' only")
            sys.exit()

    if date is not None:
        if date.lower() == 'oldest':
            clipboard_contents_sorted: dict = sort(highest=False, newest=False, sort_by_priority=False)
        elif date.lower() == 'newest':
            clipboard_contents_sorted: dict = sort(highest=False, newest=True, sort_by_priority=False)
        else:
            click.echo(Fore.RED + "Invalid option, you could put 'oldest' or 'newest' only")
            sys.exit()

    show_clipboard_contents(clipboard_contents=clipboard_contents_sorted)
