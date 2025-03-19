from htmlnode import HTMLNODE



class LeafNode(HTMLNODE):
    def __init__(self, tag, value, props={}):
        super().__init__(tag, value, [], props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        
        if self.props:
            return f'<{self.tag} {self.props_to_html().strip()}>{self.value}</{self.tag}>'
        
        return f'<{self.tag}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.children}, {self.props})"
