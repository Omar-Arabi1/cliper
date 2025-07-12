from typing import Optional
import click
from fuzzywuzzy import process
from colorama import Fore

from helpers import clipboad_context
from helpers.check_clipboard_empty import check_if_empty

@click.command(help='search through the labels you have')
@click.option('-f', '--filter', help='filter results by date for more accurate results takes in a date Y-M-D', default=None)
@click.argument('query')
def search(query: str, filter: Optional[str]) -> None:
    """
    users could use this command to search for a certain label to access it, delete it, etc it takes in a required 
    query to search with and an optional filter option which takes in the date at it was created to search only
    for items that were created at that date
    
    it fuzzy searches through the list and shows only the results with accuracy above 80%
    
    PARAMS: query: str = the query to search with
    PARAMS: filter: Optional[str] = takes in a date Y-M-D and only searches in the items that were created at this date
    
    EXAMPLE:
        >>> cliper search <query> -f <date>
        output -> <result-list>
    """
    check_if_empty()
    clipboard_contents: dict = clipboad_context.read_json()
    labels: list[str] = []
    best_matches: list[str] = []

    for copied_text in clipboard_contents:
        data: dict = clipboard_contents.get(copied_text)
        creation_date = data.get('creation_date')

        if filter is not None and creation_date == filter:
            labels.append(data.get('label'))
        elif filter is None:
            labels.append(data.get('label'))

    matches: list[tuple] = process.extract(query, labels)

    for index, _ in enumerate(matches):
        match_data = matches[index]
        accuracy: int = match_data[1]
        if accuracy >= 80:
            match: str = match_data[0]
            best_matches.append(match)

    for best_match in best_matches:
        print(Fore.GREEN + best_match)
