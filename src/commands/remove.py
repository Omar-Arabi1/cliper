from typing import Optional
import click
from colorama import Fore
import sys

from helpers import clipboad_context
from helpers.check_clipboard_empty import check_if_empty

@click.command(help='remove a copied text')
@click.option('-l', '--label', help='remove copied text with its label')
@click.option('-rp', '--remove-priority', help='remove all copied text with a certain level of priority', default=None)
@click.option('-a', '--all', help='remove all copied text at once', default=False, is_flag=True)
def remove(label: str, remove_priority: Optional[str], all: bool) -> None:
    """
    use this command to remove something from the clipboard it takes in a label option
    to remove a specific label a remove-priority option which removes everything that has
    the same provided priority (must be at least 1 and at most 3) or all option which removes
    everything 
    
    at least on of these must be included for the function to take effect
    
    PARAMS: label: str = a label to remove
    PARAMS: remove_priority: Optional[str] = if you want to remove all occurences of the same priority (it is a string because by default the entered type is)
    PARAMS: all: bool = determines wether or not to remove the entire list
    
    EXAMPLE:
        >>> click remove -a
        output -> removed all copied text
    """
    check_if_empty()
    clipboard_content: dict = clipboad_context.read_json()

    if all is True:
        clipboad_context.write_json(data_to_write={})
        click.echo(Fore.GREEN + "removed all copied text")
        sys.exit()

    for copied_text in clipboard_content:
        data: dict = clipboard_content.get(copied_text)
        if data.get('label') == label:
            click.echo(Fore.GREEN + f"removed copied text at label '{label}'")
            clipboard_content.pop(copied_text)
            clipboad_context.write_json(data_to_write=clipboard_content)
            sys.exit()

    if remove_priority is not None:
        not_removed_sequences = filter(lambda data: data[1].get('priority') != int(remove_priority), clipboard_content.items())
        not_removed_from_clipboard: dict = dict([not_removed for not_removed in not_removed_sequences])
        clipboad_context.write_json(data_to_write=not_removed_from_clipboard)
        click.echo(Fore.GREEN + f'removed all sequences that contain {remove_priority} as a priority')