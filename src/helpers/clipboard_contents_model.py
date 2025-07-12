class ClipBoardContents():
    """
    a class for the clipboard it contains its data and an 'as_dict' function which returns a 
    representation of the model as a dicionary so that it becomes json serializable
    """
    def __init__(self, clipboard_content: str, label: str, priority: int, creation_date: str) -> None:
        """
        PARAM: clipboard_content: str = the copied text that will be added
        PARAM: label: str = the label marked to this copied text for searching removing etc
        PARAM: priority: int = the priority of the text 1-3
        PARAM: creation_date: str = the date at which the text was added to the clipboard Y-M-D
        """
        self.clipboard_content: str = clipboard_content
        self.label: str = label
        self.priority: int = priority
        self.creation_date: str = creation_date
        
    def as_dict(self) -> dict:
        """ 
        the dict representation that will be saved in the .clipboard_content.json 
        
        EXAMPLE:
            >>> clipboard_content.as_dict()
            returns -> <copied_text> {
                'label': <label>,
                'priority': <priority>,
                'creation_date': <creation-date>
            }
        """
        return {
            self.clipboard_content: {
                'label': self.label,
                'priority': self.priority,
                'creation_date': self.creation_date
            }
        }