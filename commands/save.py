import click
import pyperclip
from typing import Optional

@click.command(help='save your last copied text')
@click.option('-l', '--label', help='REQUIRED: enter a label for searching')
def save_last_copied(label: Optional[str] = None) -> None:
    last_copied_text: str = pyperclip.paste()
    
    if label is None:
        click.echo("A label is required use the '--label' or '-l' options, use '--help' for more info")
        return
    
        
    