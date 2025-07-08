import click

from commands import save, remove, list, search

@click.group(help="a CLI tool to save your clipboard history")
def main() -> None:
    pass

main.add_command(save.save)
main.add_command(remove.remove)
main.add_command(list.list)
main.add_command(search.search)

if __name__ == '__main__':
    main()