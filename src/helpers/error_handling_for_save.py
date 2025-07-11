import click
from colorama import Fore

def error_handling(label: str, priority: int, last_copied_text: str, labels: list[str], last_copied_texts: list[str]) -> bool:
    if label is None:
        click.echo(Fore.RED + "A label is required use the '--label' or '-l' options, use '--help' for more info")
        return False
    
    if priority <= 0 or priority > 3:
        click.echo(Fore.RED + "A priority can't be less than zero or greater than three")
        return False
    
    if last_copied_text in last_copied_texts:
        click.echo(Fore.RED + "The copied text already exists")
        return False
            
    if label in labels:
        click.echo(Fore.RED + "The label you entered already exists")
        return False
    return True
    