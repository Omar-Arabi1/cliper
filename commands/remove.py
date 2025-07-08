import click

@click.command(help='remove a copied text')
@click.argument('label')
def remove(label: str) -> None:
    pass