from core import GameEasy
from core import GameNormal
from core import GameHard
from core import WindowMananger
import tkinter


def main():
    game = GameNormal(lang="fr_French",
                      category="colores",
                      debug=False)

    game.play_rounds(1)


if __name__ == '__main__':
    root = tkinter.Tk()
    settings = WindowMananger(root)
    settings.mainloop()




