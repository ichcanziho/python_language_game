from tkinter import ttk
import tkinter as tk
from pathlib import Path
import json
from tkinter import messagebox


class TabSettings:

    def __init__(self, nb):
        self.nb = nb
        self.window = ttk.Frame(self.nb)
        file = Path("./settings.json")
        if not file.is_file():
            self.set_default_settings()

        with open("settings.json") as json_file:
            self.current_settings = json.load(json_file)

        self.languages = None
        self.categories = None

        self.make_languages_box()
        self.make_categories_box()
        self.make_difficulty_box()
        self.make_questions_input()
        self.make_save_button()

        self.nb.add(self.window, text='Settings')

    #######################################
    #            Widget Section           #
    #######################################

    def make_languages_box(self):

        self.read_lang_available()

        self.lb_language = tk.Label(self.window, text="Idioma")
        self.lb_language.pack()

        self.languages_box = ttk.Combobox(self.window, state="readonly")
        self.languages_box.bind("<<ComboboxSelected>>", self.language_changed)
        self.languages_box["values"] = self.languages
        lang_pos = self.current_settings['target_lang']
        try:
            lang_pos = self.languages.index(lang_pos)
        except Exception:
            lang_pos = 0

        self.languages_box.current(lang_pos)
        self.languages_box.pack()

    def make_categories_box(self):
        self.read_categories_available()

        self.lb_category = tk.Label(self.window, text="Categoria")
        self.lb_category.pack()

        self.categories_box = ttk.Combobox(self.window, state="readonly")
        self.categories_box["values"] = self.categories
        cate_pos = self.current_settings['category']
        try:
            cate_pos = self.categories.index(cate_pos)
        except Exception:
            cate_pos = 0

        self.categories_box.current(cate_pos)
        self.categories_box.pack()

    def make_difficulty_box(self):
        self.difficulties = ["easy", "med", "hard"]

        self.lb_difficulty = tk.Label(self.window, text="Dificultad")
        self.lb_difficulty.pack()

        self.difficulties_box = ttk.Combobox(self.window, state="readonly")
        self.difficulties_box["values"] = self.difficulties
        dif_pos = self.current_settings['difficulty']
        dif_pos = self.difficulties.index(dif_pos)
        self.difficulties_box.current(dif_pos)
        self.difficulties_box.pack()

    def make_questions_input(self):
        self.lb_quantity = tk.Label(self.window, text="Palabras")
        self.lb_quantity.pack()

        self.in_quantity = tk.Entry(self.window, width=22)
        ques = self.current_settings['questions']
        self.in_quantity.insert(0, ques)
        self.in_quantity.pack()

    def make_save_button(self):
        self.bt_save = tk.Button(self.window, text="Guardar", command=self.save_settings)
        self.bt_save.pack(pady=10)

    #######################################
    #            Widget Actions           #
    #######################################

    def save_settings(self):
        self.set_target_lang(self.languages_box.get())
        self.set_category(self.categories_box.get())
        self.set_difficulty(self.difficulties_box.get())
        self.set_questions(self.in_quantity.get())
        if self.categories_box.get() == 'None':
            messagebox.showerror("Error", "Necesitas agregar al menos una categoria")
        else:
            self.update_settings()

    def language_changed(self, event):
        self.read_categories_available()
        self.categories_box["values"] = self.categories
        self.categories_box.current(0)

    def read_lang_available(self):
        self.languages = self.getDocuments("languages")
        if len(self.languages) == 0:
            self.languages = ['None']

    def read_categories_available(self):
        self.categories = self.getDocuments(f"languages/{self.languages_box.get()}")
        if len(self.categories) == 0:
            self.categories = ['None']

    def update_settings(self):
        messagebox.showinfo("Correcto", "Configuraciones guardadas :D")
        values = json.dumps(self.current_settings)
        file = open("settings.json", "w")
        file.write(values)
        file.close()

    #######################################
    #                Statics              #
    #######################################

    @staticmethod
    def getDocuments(path):
        objects = [obj.name for obj in Path(path).iterdir()]
        return objects

    @staticmethod
    def set_default_settings():
        settings = {"base_lang": "es",
                    "difficulty": "med",
                    "target_lang": "fr_French",
                    "category": "animales",
                    "questions": 10}
        values = json.dumps(settings)
        file = open("settings.json", "w")
        file.write(values)
        file.close()

    #######################################
    #                SETTERS              #
    #######################################

    def set_difficulty(self, dif):
        self.current_settings['difficulty'] = dif

    def set_target_lang(self, target):
        self.current_settings['target_lang'] = target

    def set_category(self, category):
        self.current_settings['category'] = category

    def set_questions(self, questions):
        self.current_settings['questions'] = questions

    def set_base_lang(self, lang):
        self.current_settings["base_lang"] = lang
