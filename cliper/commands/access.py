import click
import pyperclip
from colorama import Fore
from typing import Optional

from cliper.helpers import clipboad_context
from cliper.helpers.check_clipboard_empty import check_if_empty

"""
the access command will by default access the latest item that you have added by copying them to your clipboard,
you could overwrite that action by selecting a label for yourself use the '--label' option or '-l' for short to 
provide the label yourself

note that the label here and in any other command other than search is case sensitive and expects you to add
it fully and correctly so its recommended to add short labels you could always search for them with 'search' or
list all of them with the 'list' command
"""

@click.command(help='access the text that you copied')
@click.option('-l', '--label', help='get text with its label', default=None)
def access(label: Optional[str] = None) -> None:
    check_if_empty()
    clipboard_content: dict = clipboad_context.read_json()
    
    if label is None:
        for copied_text in reversed(clipboard_content):
            pyperclip.copy(copied_text)
            click.echo(Fore.GREEN + f"copied '{copied_text}' into your clipboard")
            return
    
    for copied_text in clipboard_content:
        data: dict = clipboard_content.get(copied_text)
        if data.get('label') == label:
            pyperclip.copy(copied_text)
            click.echo(Fore.GREEN + f"copied '{copied_text}' into your clipboard")
            return