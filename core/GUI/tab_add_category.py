from core.GUI.tables import make_table
from core import LangMaker
import pandas as pd
import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter import messagebox


class TabAddCategory:

    def __init__(self, nb):
        self.nb = nb
        self.window = ttk.Frame(self.nb)
        self.nb.add(self.window, text='Add category')

        self.languages = None
        self.categories = None

        self.settings_frame = tk.LabelFrame(self.window, text="Ajustes")
        self.settings_frame.grid(row=0, column=0, padx=10)

        self.make_languages_box()
        self.make_category_name_input()
        self.make_mode_box()
        self.make_save_button()

        self.target_lang = self.languages_box.get().split("_")[0]
        self.manual_mode = {"es": ["hola"], self.target_lang: ["hi"]}
        self.auto_mode = {"es": ["hola"]}
        self.current_mode = self.manual_mode

        self.inputs_frame = tk.LabelFrame(self.window, text="Ejemplos")
        self.inputs_frame.grid(row=0, column=1, padx=10)

        self.table = make_table(self.inputs_frame, pd.DataFrame(self.current_mode), width=180,
                                height=150, editable=True)

    #######################################
    #            Widget Section           #
    #######################################
    def make_languages_box(self):

        self.read_lang_available()
        self.lb_language = tk.Label(self.settings_frame, text="Idioma")
        self.lb_language.pack()
        self.languages_box = ttk.Combobox(self.settings_frame, state="readonly")
        self.languages_box.bind("<<ComboboxSelected>>", self.language_changed)
        self.languages_box["values"] = self.languages
        self.languages_box.current(0)
        self.languages_box.pack()

    def make_category_name_input(self):
        self.lb_category = tk.Label(self.settings_frame, text="Nombre de la Categoria")
        self.lb_category.pack()
        self.in_category = tk.Entry(self.settings_frame, width=22)
        self.in_category.insert(0, "test")
        self.in_category.pack()

    def make_mode_box(self):
        self.modes = ["manual", "auto"]

        self.lb_modes = tk.Label(self.settings_frame, text="Modo de creación")
        self.lb_modes.pack()

        self.modes_box = ttk.Combobox(self.settings_frame, state="readonly")
        self.modes_box.bind("<<ComboboxSelected>>", self.mode_changed)
        self.modes_box["values"] = self.modes
        self.modes_box.current(0)
        self.modes_box.pack()

    def make_save_button(self):
        self.bt_save = tk.Button(self.settings_frame, text="Guardar", command=self.save_settings)
        self.bt_save.pack(pady=10)

    def save_settings(self):

        if self.in_category.get() == '':
            messagebox.showerror("Error", "Necesitas ponerle nombre a tu categoria")
        else:
            dataFrame = self.table.model.df
            language = LangMaker(lang_folder=self.languages_box.get())
            if self.modes_box.get() == "manual":
                words = []
                for ori, target in zip(dataFrame['es'], dataFrame[self.target_lang]):
                    words.append([ori, target])

                language.make_new_category(category_name=self.in_category.get(),
                                           example=words, automatic_translate=False)

            else:
                words = list(dataFrame['es'])
                print(words)
                language.make_new_category(category_name=self.in_category.get(),
                                           example=words, automatic_translate=True)
            messagebox.showinfo("Correcto", "Tus palabras han sido agregadas :D")

    def language_changed(self, event):
        self.target_lang = self.languages_box.get().split("_")[0]
        self.manual_mode = {"es": ["hola"], self.target_lang: ["hi"]}
        if self.modes_box.get() == "manual":
            self.current_mode = self.manual_mode
        else:
            self.current_mode = self.auto_mode

        self.table.destroy()
        self.table = make_table(self.inputs_frame, pd.DataFrame(self.current_mode), width=180,
                                height=150,editable=True)

    def mode_changed(self, event):
        if self.modes_box.get() == "manual":
            self.current_mode = self.manual_mode
        else:
            self.current_mode = self.auto_mode
        self.table.destroy()
        self.table = make_table(self.inputs_frame, pd.DataFrame(self.current_mode), width=180,
                                height=150,editable=True)

    def read_lang_available(self):
        self.languages = self.getDocuments("languages")
        if len(self.languages) == 0:
            self.languages = ['None']

    @staticmethod
    def getDocuments(path):
        objects = [obj.name for obj in Path(path).iterdir()]
        return objects