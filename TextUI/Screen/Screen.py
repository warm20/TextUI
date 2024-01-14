from TextUI.Style import *
from TextUI.CurCtrl import Curser

class Screen:
    def __init__(self, w, h, title, 
                 title_style=LEFT, border_style=SOFT_BORDER
    ) -> None:
        self.w,self.h = int(w),int(h)
        self.title = title
        self.title_style = title_style
        self.border = border_style
        self.cur = Curser.Curser()
        pass

    def DrawScreen(self):
        self.cur.Clear()
        self.cur.MoveTo(0,0)
        # Draw top bar
        print(self.border[L_T],end="")
        for i in range(self.w):
            print(self.border[LINE],end="")
        print(self.border[R_T]+"\033[K")
        # Draw title
        if len(self.title)>self.w:
            self.cur.MoveTo(2,0)
            print(self.title[0:self.w],end="")
        else:
            if self.title_style == LEFT:
                self.cur.MoveTo(2,0)
                print(self.title,end="")
            elif self.title_style == RIGHT:
                self.cur.MoveTo(self.w-len(self.title)+2,0)
                print(self.title, end="")
            else:
                ms = (self.w//2-len(self.title)//2)%2
                self.cur.MoveTo(
                    self.w//2-len(self.title)//2+int("12"[ms]),
                    0
                )
                print(self.title, end="")
                ...

        # Draw body
        for i in range(self.h):
            self.cur.MoveTo(0,i+2)
            print(self.border[VER], end="")
            self.cur.MoveTo(self.w+2,i+2)
            print(self.border[VER], end="")
        print()
        # Draw bottom
        print(self.border[L_B],end="")
        for i in range(self.w):
            print(self.border[LINE],end="")
        print(self.border[R_B])
    
