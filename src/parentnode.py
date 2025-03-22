from htmlnode import *

class ParentNode(HTMLNODE):
    def __init__(self, tag, children, props={}):
        super().__init__(tag, None,children, props)
    
    def add_child(self, child):
        self.children.append(child)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")

        html = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            html += child.to_html()
        html += f'</{self.tag}>'
        return html