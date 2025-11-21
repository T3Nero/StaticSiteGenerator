import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, World!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(), ' class="greeting" href="https://boot.dev"'
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )
        
class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_and_props(self):
        leaf = LeafNode(
            tag="a",
            value="Click here",
            props={"href": "https://boot.dev", "class": "link"},
        )
        expected_html = '<a href="https://boot.dev" class="link">Click here</a>'
        self.assertEqual(leaf.to_html(), expected_html)

    def test_to_html_with_tag_no_props(self):
        leaf = LeafNode(
            tag="span",
            value="Just some text",
        )
        expected_html = "<span>Just some text</span>"
        self.assertEqual(leaf.to_html(), expected_html)

    def test_to_html_no_tag(self):
        leaf = LeafNode(
            value="Plain text without a tag",
        )
        expected_html = "Plain text without a tag"
        self.assertEqual(leaf.to_html(), expected_html)


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_children_and_props(self):
        child1 = LeafNode(tag="li", value="Item 1")
        child2 = LeafNode(tag="li", value="Item 2")
        parent = ParentNode(
            tag="ul",
            children=[child1, child2],
            props={"class": "item-list"},
        )
        expected_html = '<ul class="item-list"><li>Item 1</li><li>Item 2</li></ul>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_to_html_with_children_no_props(self):
        child1 = LeafNode(tag="p", value="Paragraph 1")
        child2 = LeafNode(tag="p", value="Paragraph 2")
        parent = ParentNode(
            tag="div",
            children=[child1, child2],
        )
        expected_html = "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>"
        self.assertEqual(parent.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()