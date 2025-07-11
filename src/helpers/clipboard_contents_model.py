class ClipBoardContents():
    def __init__(self, clipboard_content: str, label: str, priority: int) -> None:
        self.clipboard_content: str = clipboard_content
        self.label: str = label
        self.priority: int = priority
        
    def as_dict(self) -> dict:
        return {
            self.clipboard_content: {
                'label': self.label,
                'priority': self.priority
            }
        }