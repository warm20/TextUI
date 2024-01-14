from TextUI.Style import *

class Screen:
    def __init__(self, w, h, title, 
                 title_style=LEFT, border_style=SOFT_BORDER
    ) -> None:
        self.w,self.h = int(w),int(h)
        self.title = title
        self.title_style = title_style
        self.border = border_style
        pass

    def DrawScreen(self):
        border = ""
        if self.border == HARD_BORDER:
            border = "└┘┌┐─"
        elif self.border == SOFT_BORDER:
            border = "╰╯╭╮─"