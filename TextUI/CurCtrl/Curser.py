class Curser:
    def __init__(self) -> None:
        pass
    def MoveTo(self, x:int, y:int):
        print("\033[%d;%dH"%(y,x), end="")
    def Clear(self):
        print("\033[2J", end="")
    def Hide(self):
        print("\033[?25l", end="")
    def Show(self):
        print("\033[?25h", end="")
    def ClearBuff(self):
        print("\033[0m" ,end="")
    
