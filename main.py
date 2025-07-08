import click

from commands import save

@click.group(help="a CLI tool to save your clipboard history")
def main() -> None:
    pass

main.add_command(save.save_last_copied())

if __name__ == '__main__':
    main()