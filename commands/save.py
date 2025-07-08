import click
import pyperclip
from typing import Optional
from helpers import clipboad_context

@click.command(help='save your last copied text')
@click.option('-l', '--label', help='REQUIRED: enter a label for searching')
@click.option('-p', '--priority', help='set a priority for this text highest 3 lowest 1', default=1)
def save_last_copied(priority: int, label: Optional[str] = None) -> None:
    clipboard_context_read: dict = clipboad_context.read_json()
    last_copied_text: str = pyperclip.paste()
    
    if label is None:
        click.echo("A label is required use the '--label' or '-l' options, use '--help' for more info")
        return
    
    if priority <= 0:
        click.echo("A priority can't be less than zero")
        return 
    
    if last_copied_text in list(clipboard_context_read.keys):
        last_copied_text_label: str = clipboard_context_read.get(last_copied_text).get('label')
        click.echo(f"The copied text already exists as label {last_copied_text_label}")
        return
    
    
    
        
    