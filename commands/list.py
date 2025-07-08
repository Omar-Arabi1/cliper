import click

from helpers import clipboad_context

@click.command(help='list through all the saved copied texts you have')
def list() -> None:
    cliboard_contents: dict = clipboad_context.read_json()
    
    for copied_text in cliboard_contents:
        data: dict = cliboard_contents.get(copied_text)
        label: str = data.get('label')
        prioirty: int = data.get('priority')
        print(f"{label}) '{copied_text}' -priority {prioirty}")
