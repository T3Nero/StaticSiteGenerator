import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a bold text node", TextType.BOLD)
        node3 = TextNode("This is an italic text node", TextType.ITALIC)
        node4 = TextNode("This is a text node with a URL", TextType.BOLD, URL="https://boot.dev")
        node5 = TextNode("This is a text node without a URL", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node4, node5)
        


if __name__ == "__main__":
    unittest.main()