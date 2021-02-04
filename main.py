from core import GameEasy
from core import GameNormal
from core import GameHard
from core import WindowMananger
import tkinter


if __name__ == '__main__':
    root = tkinter.Tk()
    settings = WindowMananger(root)
    settings.mainloop()




