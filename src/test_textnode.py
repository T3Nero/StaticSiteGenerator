import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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


    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        


if __name__ == "__main__":
    unittest.main()