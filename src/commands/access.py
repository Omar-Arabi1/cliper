import click
import pyperclip
from colorama import Fore
from typing import Optional
import sys

from helpers import clipboad_context
from helpers.check_clipboard_empty import check_if_empty

@click.command(help='access the text that you copied')
@click.option('-l', '--label', help='get text with its label', default=None)
def access(label: Optional[str] = None) -> None:
    """
    this command is used when the user wants to access something they saved in the clipboard
    by default it accesses the latest given thing that action could be overwritten by providing
    your own label with `-l`
    
    PARAMS: label: Optional[str] = if you want to override the default behavior of what gets retrieved by something known you could provide its label
    
    EXAMPLE:
        >>> cliper access -l <label>
        output -> copied '<text>' into your clipboard"
    
    NOTE: if no output was given that means the label doesn't exist
    """
    check_if_empty()
    clipboard_content: dict = clipboad_context.read_json()
    
    if label is None:
        for copied_text in reversed(clipboard_content):
            pyperclip.copy(copied_text)
            click.echo(Fore.GREEN + f"copied '{copied_text}' into your clipboard")
            sys.exit()
    
    for copied_text in clipboard_content:
        data: dict = clipboard_content.get(copied_text)
        if data.get('label') == label:
            pyperclip.copy(copied_text)
            click.echo(Fore.GREEN + f"copied '{copied_text}' into your clipboard")
            sys.exit()