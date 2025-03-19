class HTMLNODE:
    def __init__(self, tag =None , value=None, children=[], props={}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("This method should be overriden by the subclass")
    
    def props_to_html(self):
        if not self.props:
            return ''
        for k,v in self.props.items():
            return f'{k}="{v}" '
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

