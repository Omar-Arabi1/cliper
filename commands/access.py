import click
import pyperclip

from helpers import clipboad_context
from helpers.check_clipboard_empty import check_if_empty

@click.command(help='access the text that you copied')
@click.option('--no-latest', help='get the latest one you entered', default=True, is_flag=True)
@click.option('-l', '--label', help='get text with its label')
def access(label: str, no_latest: bool = False) -> None:
    check_if_empty()
    clipboard_content: dict = clipboad_context.read_json()
    
    if no_latest is True:
        for copied_text in reversed(clipboard_content):
            pyperclip.copy(copied_text)
            click.echo(f"copied '{copied_text}' into your clipboard")
            return
        
    for copied_text in clipboard_content:
        data: dict = clipboard_content.get(copied_text)
        if data.get('label') == label:
            pyperclip.copy(copied_text)
            click.echo(f"copied '{copied_text}' into your clipboard")
            return