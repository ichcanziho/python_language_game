from tkinter import ttk
import tkinter as tk
from googletrans import LANGUAGES
import pandas as pd
from pathlib import Path
from core import LangMaker
from tkinter import messagebox


class TabLanguage:

    def __init__(self, nb):

        self.nb = nb
        self.window = ttk.Frame(self.nb)
        self.lb_sentence_lang = None
        self.combobox_language = None
        self.bt_make_language = None
        self.language_path = "languages"
        self.example_categories_path = "examples/base_categories"
        self.support_languages = LANGUAGES
        self.support_languages_reverse = {value: key for key, value in self.support_languages.items()}
        self.make_new_language_picker()

        self.nb.add(self.window, text='Add Language')

    def make_new_language_picker(self):
        self.lb_sentence_lang = tk.Label(self.window, text="Agrega un lenguaje", pady=10)
        self.lb_sentence_lang.pack(pady=10)

        self.combobox_language = ttk.Combobox(self.window, state="readonly")
        self.combobox_language["values"] = list(self.support_languages.values())
        self.combobox_language.current(0)
        self.combobox_language.pack(pady=20)
        self.bt_make_language = tk.Button(self.window, text="Crear nuevo lenguaje", width=30, height=3,
                                          bg="CadetBlue1", command=self.action_bt_make_language)
        self.bt_make_language.pack(pady=20)

    def action_bt_make_language(self):
        lang = self.combobox_language.get()
        name = self.support_languages_reverse.get(lang, "")
        if name != "":
            folder = f'{name}_{lang}'
            categories = self.getDocuments(self.example_categories_path)
            if not (Path(f'{self.language_path}/{folder}').is_dir()):
                Path.mkdir(Path(f'{self.language_path}/{folder}'))
            language = LangMaker(lang_folder=folder)
            for category in categories:
                if not (Path(f'{folder}/{category}').is_dir()):
                    new_path = f'{self.example_categories_path}/{category}/{category}.csv'
                    frame = pd.read_csv(new_path)
                    words = list(frame["es"])
                    language.make_new_category(category_name=category, example=words, automatic_translate=True)

            messagebox.showinfo("Correcto", "Se ha creado tu nuevo idioma :D\n Es necesario reiniciar para ver los cambios.")
        else:
            messagebox.showerror("Error", "este idioma no se ha podido agregar :(")

    @staticmethod
    def getDocuments(path):
        objects = [obj.name for obj in Path(path).iterdir()]
        return objects

