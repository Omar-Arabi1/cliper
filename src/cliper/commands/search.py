import click
from fuzzywuzzy import process
from colorama import Fore

from helpers import clipboad_context
from helpers.check_clipboard_empty import check_if_empty

"""
with this command you could search all of your labels, but you don't need to enter their names exactly
since this is a fuzzy search basically you could enter a part of the label and it will give you the best matches

example:
./cliper.pyz search cl
1) clock
2) clack 

of course that just means that in the list you have there is a clock and a clack and maybe more, but they just didn't get
included because they didn't pass the 80% accuracy limit set you could then access them or remove them with using the label
that matched the label in mind 

note that I didn't implement this fuzzy finding algorithm on my own I used a package named fuzzywuzzy and it did most of the 
hardwork I just filtered out the the matches that were past 80% on accuracy
"""

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
        print(f"{Fore.CYAN + str(num_of_match)}) {Fore.BLUE + best_match}")