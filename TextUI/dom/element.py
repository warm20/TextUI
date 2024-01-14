class Element:
    # pos (x,y) is the left and top
    # the element draw view will from pos(x,y) to (x+w,y+h)
    def __init__(self,x,y,w,h) -> None:
        self.x,self.y = x,y
        self.w,self.h = w,h
        pass
