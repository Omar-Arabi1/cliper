import click
import pyperclip

from helpers import clipboad_context

@click.command(help='access the text that you copied')
@click.option('-la', '--latest', help='get the latest one you entered', default=False, is_flag=True)
@click.option('-l', '--label', help='get text with its label')
def access(label: str, latest: bool = False) -> None:
    clipboard_content: dict = clipboad_context.read_json()
    
    if latest is True:
        for copied_text in reversed(clipboard_content):
            pyperclip.copy(copied_text)
            click.echo(f"copied '{copied_text}' into your clipboard")
            return
        