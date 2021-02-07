from core import WindowMananger
import tkinter


def main():
    root = tkinter.Tk()
    settings = WindowMananger(root)
    settings.mainloop()


if __name__ == '__main__':
    main()



