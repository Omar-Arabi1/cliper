from .json import Json
import getpass

user: str = getpass.getuser()
clipboad_context: Json = Json(f'/home/{user}/.clipboard_contents.json')
clipboad_context.create_data_file()