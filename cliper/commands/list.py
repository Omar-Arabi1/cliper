import click
from colorama import Fore

from cliper.helpers import clipboad_context
from cliper.helpers.sort_highest_priority import sort_highest_priority
from cliper.helpers.check_clipboard_empty import check_if_empty

"""
with this command you will get a table-like format with all the data it will start with the label text 
and then the priority by default it will print them with the order at which they are saved at in the json file
you could use the '--sort-by-heighest-priority' option or '-shp' for short to sort them by the priorities value
the highest first of course

note that there is no function in python that sorts based on a value in a dictionary and then sorts the dictionary's keys
themselves so in helpers/sort_highest_priority.py file there is a way that I managed to get it for more info go to that file
"""

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