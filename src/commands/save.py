import click
import pyperclip
from typing import Optional
from colorama import Fore
import datetime

from helpers.clipboard_contents_model import ClipBoardContents
from helpers import clipboad_context
from helpers.error_handling_for_save import error_handling

@click.command(help='save your last copied text')
@click.option('-l', '--label', help='REQUIRED: enter a label for searching')
@click.option('-p', '--priority', help='set a priority for this text highest 3 lowest 1', default=1)
def save(priority: int, label: Optional[str] = None) -> None:
    """
    this command is used when you want to save the first thing in the clipboard it takes
    in a label and an optional priority and it adds in a date automatically and by default
    the priority is 1
    
    PARAMS: priority: int = takes in the priority which is 1 by default (lowest 3 highest) it doesn't take anything lower than 1 or higher than 3
    PARAMS: label: Optional[str] = takes in the required label by default its None
    
    EXAMPLE:
        >>> cliper save --label <label> -p <priority>
        output -> saved item
    """
    clipboard_contents: dict = clipboad_context.read_json()
    last_copied_text: str = pyperclip.paste()
    last_copied_texts: list[str] = []
    labels: list[str] = []

    for copied_text in clipboard_contents:
        last_copied_texts.extend(list(clipboard_contents.keys()))
        labels.extend(list(clipboard_contents.get(copied_text).values()))

    error_handling(label=label, priority=priority, last_copied_text=last_copied_text, labels=labels, last_copied_texts=last_copied_texts)

    current_time: datetime = datetime.datetime.now()
    current_date = str(current_time.date())

    new_clipbaord_item: ClipBoardContents = ClipBoardContents(
        clipboard_content=last_copied_text,
        label=label,
        priority=priority,
        creation_date=current_date
    )

    clipboard_contents.update(new_clipbaord_item.as_dict())

    clipboad_context.write_json(data_to_write=clipboard_contents)
    click.echo(Fore.GREEN + 'saved item')
