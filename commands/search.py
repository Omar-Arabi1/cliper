import click
from fuzzywuzzy import process
import sys

from helpers import clipboad_context
from helpers.check_clipboard_empty import check_if_empty

@click.command(help='search through the labels you have')
@click.argument('query')
def search(query: str) -> None:
    check_if_empty()
    clipboard_contents: dict = clipboad_context.read_json()
    labels: list[str] = []
    
    for copied_text in clipboard_contents:
        data: dict = clipboard_contents.get(copied_text)
        labels.append(data.get('label'))
    
    matches: list[tuple] = process.extract(query, labels)
    best_matches: list[str] = []
    
    for index in range(len(matches)):
        match_data: tuple = matches[index]
        accuracy: int = match_data[1]
        if accuracy >= 80:
            match: str = match_data[0]
            best_matches.append(match)
    
    for index, best_match in enumerate(best_matches):
        num_of_match: int = index + 1
        print(f"{num_of_match}) {best_match}")