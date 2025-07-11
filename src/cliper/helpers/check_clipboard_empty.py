import sys, click
from colorama import Fore

from . import clipboad_context

def check_if_empty() -> None:
    clipboard_contents: dict = clipboad_context.read_json()
    
    if len(clipboard_contents) == 0:
        click.echo(Fore.RED + "Your clipboard is empty use the 'save' command to add something use '--help' for more detail")
        sys.exit() 