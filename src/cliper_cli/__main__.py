#!/usr/bin/env python3

import click

from . import __version__
from commands import save, remove, list, search, access

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