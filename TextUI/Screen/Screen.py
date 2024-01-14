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
        self.frame = [[" " for i in range(h)] for j in range(w)]
        pass

    def DrawScreen(self):
        # Draw top bar
        print(self.border[L_T],end="")
        for i in range(self.w):
            print(self.border[LINE],end="")
        print(self.border[R_T]+"\033[K")
        # Draw body
        for i in range(self.h):
            print(self.border[VER],end="")
            for j in range(self.w):
                print(self.frame[j][i], end="")
            print(self.border[VER])
        # Draw bottom
        print(self.border[L_B],end="")
        for i in range(self.w):
            print(self.border[LINE],end="")
        print(self.border[R_B])