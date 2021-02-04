import tkinter as tk
from tkinter import ttk
from core.GUI import TabSettings


class WindowMananger(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Hola")
        nb = ttk.Notebook(self.master)
        nb.pack(fill='both', expand='yes')
        TabSettings(nb)


def main():

    root = tk.Tk()
    log = WindowMananger(root)
    log.mainloop()

    print("Program Execution Completed")


if __name__ == "__main__":
    main()
