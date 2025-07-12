import click
from colorama import Fore
import sys

def error_handling(label: str, priority: int, last_copied_text: str, labels: list[str], last_copied_texts: list[str]) -> None:
    """
    a function that does the error handling for the save command 
    this fucntion doesn't allow for duplicate labels or text
    
    PARAM: label: str = the label that will be saved with the text
    PARAM: priority: int = the priority level that will be saved with the text 1-3
    PARAM: last_copied_text: str = the text itself
    PARAM: labels: list[str] = the list of labels to check if the given label already exists
    PARAM: last_copied_texts: list[str] = a list of all the text inside of the clipboard to check if the new one already exists
    
    EXAMPLE:
        >>> error_handling()
        example_output: A label is required use the '--label' or '-l' options, use '--help' for more info
    """
    if label is None:
        click.echo(Fore.RED + "A label is required use the '--label' or '-l' options, use '--help' for more info")
        sys.exit()

    if priority <= 0 or priority > 3:
        click.echo(Fore.RED + "A priority can't be less than zero or greater than three")
        sys.exit()

    if last_copied_text in last_copied_texts:
        click.echo(Fore.RED + "The copied text already exists")
        sys.exit()

    if label in labels:
        click.echo(Fore.RED + "The label you entered already exists")
        sys.exit()
