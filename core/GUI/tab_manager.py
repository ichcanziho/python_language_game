import tkinter as tk
from tkinter import ttk
from core.GUI import TabSettings
from core.GUI import TabAddCategory
from core.GUI import TabPlay
from core.GUI import TabLanguage


class WindowManager(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Python Language Game by Ichcanziho")
        nb = ttk.Notebook(self.master)
        nb.pack(fill='both', expand='yes')
        TabPlay(nb)
        TabSettings(nb)
        TabAddCategory(nb)
        TabLanguage(nb)
