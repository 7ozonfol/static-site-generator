import unittest

from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNODE('div')
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})
    
    def test_repr(self):
        node = HTMLNODE('div')
        self.assertEqual(repr(node), "HTMLNode(div, None, [], {})")
    
    def test_props_to_html(self):
        node = HTMLNODE('div', props={'class':'container'})
        self.assertEqual(node.props_to_html().lstrip(), 'class="container" ')



if __name__ == "__main__":
    unittest.main()