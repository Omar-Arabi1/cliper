import click

from helpers import clipboad_context

@click.command(help='remove a copied text')
@click.argument('label')
def remove(label: str) -> None:
    clipboard_content: dict = clipboad_context.read_json()
    
    for copied_text in clipboard_content:
        data: dict = clipboard_content.get(copied_text)
        if data.get('label') == label:
            click.echo(f"removed copied text at label '{label}'")
            clipboard_content.pop(copied_text)
            clipboad_context.write_json(data_to_write=clipboard_content)
            return
    
    click.echo("The label doesn't exist")