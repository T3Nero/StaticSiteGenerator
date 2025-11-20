from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, URL=None):
        self.text = text
        self.type = text_type
        self.url = URL

    def __eq__(self, other):
        return (
            self.type == other.type
            and self.text == other.text
            and self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"
    
