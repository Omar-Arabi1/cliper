import click
from colorama import Fore

from helpers import clipboad_context
from helpers.sort_highest_priority import sort_highest_priority
from helpers.check_clipboard_empty import check_if_empty

@click.command(help='list through all the saved copied texts you have')
@click.option('-shp', '--sort-by-heighest-priority', help='print the list sorted from highest priority rank', default=False, is_flag=True)
def list(sort_by_heighest_priority: bool) -> None:
    check_if_empty()
    clipboard_contents: dict = clipboad_context.read_json()
    label_lengths: list[int] = []
    text_lengths: list[int] = []
    
    for copied_text in clipboard_contents:
        data: dict = clipboard_contents.get(copied_text)
        label: str = data.get('label')
        label_lengths.append(len(label))
        text_lengths.append(len(copied_text))

    label_padding: int = max(label_lengths) + 1
    text_padding: int = max(text_lengths) + 1
    
    if sort_by_heighest_priority is True:
        clipboard_contents_updated: dict = sort_highest_priority()
        for copied_text in clipboard_contents_updated:
            data: dict = clipboard_contents.get(copied_text)
            label: str = data.get('label')
            prioirty: str = str(data.get('priority'))
            print(f"{Fore.GREEN + label.ljust(label_padding)}) {Fore.CYAN + copied_text.ljust(text_padding)} -prioirty {Fore.RED + prioirty}")
    
    if sort_by_heighest_priority is False: 
        for copied_text in clipboard_contents:
            data: dict = clipboard_contents.get(copied_text)
            label: str = data.get('label')
            prioirty: str = str(data.get('priority'))
            print(f"{Fore.GREEN + label.ljust(label_padding)}) {Fore.CYAN + copied_text.ljust(text_padding)} -prioirty {Fore.RED + prioirty}")