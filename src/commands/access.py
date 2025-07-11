import click
import pyperclip
from colorama import Fore
from typing import Optional

from helpers import clipboad_context
from helpers.check_clipboard_empty import check_if_empty

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