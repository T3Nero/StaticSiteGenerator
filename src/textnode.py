from enum import Enum
from htmlnode import LeafNode

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
    
    
def text_node_to_html_node(text_node):
    if text_node.type == TextType.TEXT:
        return LeafNode(value=text_node.text)
    elif text_node.type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.type == TextType.IMAGE:
        return LeafNode(tag="img", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported text type: {text_node.type}")