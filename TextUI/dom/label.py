import dom.element as ele

class Label(ele.Element):
    def __init__(self, x, y, w, h,content) -> None:
        super().__init__(x, y, w, h)
        if self.w < len(content):
            content = content[0:self.w]
        self.content = content
    def Draw(self):
        ...