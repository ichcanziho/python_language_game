from core import WindowManager
import tkinter


def main():
    root = tkinter.Tk()
    settings = WindowManager(root)
    settings.mainloop()


if __name__ == '__main__':
    main()
