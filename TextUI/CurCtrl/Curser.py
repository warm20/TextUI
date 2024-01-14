class Curser:
    def __init__(self) -> None:
        pass
    def MoveTo(self, x:int, y:int):
        print("\33[%d;%d"%(y,x), end="")
    def Clear(self):
        print("\33[2J", end="")
    def Hide(self):
        print("\33[?25l", end="")
    def Show(self):
        print("\33[?25h", end="")
    def ClearBuff(self):
        print("\33[0m" ,end="")
    
