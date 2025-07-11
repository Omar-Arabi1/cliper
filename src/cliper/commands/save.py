import click
import pyperclip
from typing import Optional
from colorama import Fore

from helpers import clipboad_context
from helpers.error_handling_for_save import error_handling

"""
with the save command you can save the last thing in your clipboard history so the last thing you copied will be saved
it takes a required '--label' option to set its label its neccessary because you search, access, remove with the label 
I recommend using short labels to remember them if needed 

it also takes in an optional '--priority' option or '-p' for short it takes in a number to represent its importance 
from 1 min to 3 max anything lower or higher won't be accepted if you don't enter a priority it will opt to 1 by default

note that this command has the most error handling of the bunch here you only see 'error_handling' functioin being called 
for more detail on that function go to helpers/error_handling_for_save.py
"""

@click.command(help='save your last copied text')
@click.option('-l', '--label', help='REQUIRED: enter a label for searching')
@click.option('-p', '--priority', help='set a priority for this text highest 3 lowest 1', default=1)
def save(priority: int, label: Optional[str] = None) -> None:
    clipboard_content: dict = clipboad_context.read_json()
    last_copied_text: str = pyperclip.paste()
    
    for copied_text in clipboard_content:
        last_copied_texts: list[str] = list(clipboard_content.keys())
        labels: list[str] = list(clipboard_content.get(copied_text).values())
        if error_handling(label=label, priority=priority, last_copied_text=last_copied_text, labels=labels, last_copied_texts=last_copied_texts) is False:
            return 
    
    clipboard_content.update({
        last_copied_text: {
            'priority': priority, 
            'label': label
        }
    })
    
    clipboad_context.write_json(data_to_write=clipboard_content)
    click.echo(Fore.GREEN + 'saved item')