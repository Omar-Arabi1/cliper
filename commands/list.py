import click

from helpers import clipboad_context

@click.command(help='list through all the saved copied texts you have')
def list() -> None:
    clipboard_contents: dict = clipboad_context.read_json()
    label_lengths: list[int] = []
    text_lengths: list[int] = []
    
    for copied_text in clipboard_contents:
        data: dict = clipboard_contents.get(copied_text)
        label: str = data.get('label')
        label_lengths.append(len(label))
        text_lengths.append(len(copied_text))

    label_padding: int = max(label_lengths) + 1
    text_padding: int = max(text_lengths) + 1
    
    for copied_text in clipboard_contents:
        data: dict = clipboard_contents.get(copied_text)
        label: str = data.get('label')
        prioirty: str = str(data.get('priority'))
        print(f"{label.ljust(label_padding)}) {copied_text.ljust(text_padding)} -prioiryt {prioirty}")