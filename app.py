from TextUI.Screen import Screen
from TextUI.CurCtrl import Curser
from TextUI.Style import *

cur = Curser.Curser()
s = Screen.Screen(
    20,10,
    "Hello",
    border_style=SOFT_BORDER,
    title_style=CENTER
)
s.DrawScreen()