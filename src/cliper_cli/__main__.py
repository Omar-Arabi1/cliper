#!/usr/bin/env python3

import click

from . import __version__
from commands import save, remove, list_contents, search, access

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
prog_name: str = 'cliper'
@click.group(context_settings=CONTEXT_SETTINGS, help="a CLI tool to save your clipboard history")
@click.version_option(__version__, '-v', '--version', prog_name=prog_name, message=f'{prog_name} v{__version__}')
def main() -> None:
    pass

main.add_command(save.save)
main.add_command(remove.remove)
main.add_command(list_contents.list_contents)
main.add_command(search.search)
main.add_command(access.access)

if __name__ == '__main__':
    main()