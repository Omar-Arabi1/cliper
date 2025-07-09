#!/usr/bin/env python3

import click

from . import __version__
from cliper.commands import save, remove, list, search, access

"""
this project is a cli clipboard history manager, but rather than taking anything you copy you manually tell it to 
put the latest thing in your clipboard history with a label and an optional priority for searching and removing or 
any action that you will do with the text like accessing it to your clipboard history you will use the label

you could search for labels with a fuzzy search algorithm implemented from fuzzywuzzy package you could also
list them remove from them and you could access them with the access command by default this will put the latest
thing you added into your clipboard history you could use its label to access another one manually

another important thing is in the save command (the one where you add the copied text) you can't have duplicate text or labels
and the priority you add has to be at least 1 and at most 3

note that in any of the commands if there was no output except for the search command there was an issue that happend or you 
entered something wrong so it got no output to give as for the search command it just didn't find anything from your query

note that this app saves your list in a hidden json file created when you use this program at path ~/.clipboard_contents.json 

I hope you like from this project and have fun and even a bit of usefullness when using it and learn from it as
much as I did thanks for copying, downloading the tool or even checking this repo!
"""

prog_name: str = 'cliper'
@click.group(help="a CLI tool to save your clipboard history")
@click.version_option(__version__, prog_name=prog_name, message=f'{prog_name} v{__version__}')
def main() -> None:
    pass

main.add_command(save.save)
main.add_command(remove.remove)
main.add_command(list.list)
main.add_command(search.search)
main.add_command(access.access)

if __name__ == '__main__':
    main()