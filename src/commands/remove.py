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
    check_if_empty()
    clipboard_content: dict = clipboad_context.read_json()
    remove_from_clipboard_content: dict = {}
    
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
        if not remove_priority is None:
            remove_priority_as_num: int = int(remove_priority)
            if data.get('priority') != remove_priority_as_num:
                remove_from_clipboard_content.update({
                    copied_text:{
                        'label': data.get('label'), 
                        'priority': data.get('priority')
                    }
                })
                clipboad_context.write_json(data_to_write=remove_from_clipboard_content)
            else:
                click.echo(Fore.GREEN + f'removed {copied_text}')