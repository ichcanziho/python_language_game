from core import LangMaker
import pandas as pd
import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext


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

        self.make_source_input()

        self.manual_mode = {"es": ["hola"], self.target_lang: ["hi"]}
        self.auto_mode = {"es": ["hola"]}
        self.current_mode = self.manual_mode

        self.base_words_loaded = []
        self.target_words_loaded = []
    #######################################
    #            Widget Section           #
    #######################################

    def make_source_input(self):

        self.target_lang = self.languages_box.get().split("_")[0]

        self.inputs_frame = tk.LabelFrame(self.window, text="Ejemplos")
        self.inputs_frame.grid(row=0, column=1, padx=10)

        self.lb_base_lang = tk.Label(self.inputs_frame, text="es")
        self.lb_base_lang.grid(row=0, column=0)

        self.textBox_source = scrolledtext.ScrolledText(self.inputs_frame, height=9.5, width=10)
        self.textBox_source.grid(row=1, column=0)

        self.lb_target_lang = tk.Label(self.inputs_frame, text=self.target_lang)
        self.lb_target_lang.grid(row=0, column=1)

        self.textBox_output = scrolledtext.ScrolledText(self.inputs_frame, height=9.5, width=10)
        self.textBox_output.grid(row=1, column=1)

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
        auxFrame = tk.Frame(self.settings_frame)
        auxFrame.pack()
        self.in_category = tk.Entry(auxFrame, width=18)
        self.in_category.insert(0, "test")
        self.in_category.pack(side=tk.LEFT)
        self.bt_search = tk.Button(auxFrame, text="?", bg='turquoise2', command=self.check_for_category)
        self.bt_search.pack(side=tk.LEFT)

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
        self.bt_save.config(state="disable")

    def save_settings(self):

        self.flag_error_manual = False
        if self.in_category.get() == '':
            messagebox.showerror("Error", "Necesitas ponerle nombre a tu categoria")
        else:
            source = self.textBox_source.get('1.0', "end")
            source = source.split("\n")
            clean_source = []
            source = [word for word in source if word != ""]
            clean_source = [word for word in source if word not in clean_source]
            source = clean_source
            target = self.textBox_output.get('1.0', "end")
            target = target.split("\n")
            target = [word for word in target if word != ""]

            new_target_words = [word for word in target if word not in self.target_words_loaded]
            new_base_words = [word for word in source if word not in self.base_words_loaded]

            source = new_base_words
            target = new_target_words

            language = LangMaker(lang_folder=self.languages_box.get())
            if self.modes_box.get() == "manual":
                if len(target) == len(source):
                    words = []
                    for ori, tar in zip(source, target):
                        words.append([ori, tar])

                    language.make_new_category(category_name=self.in_category.get(),
                                               example=words, automatic_translate=False)

                else:
                    tk.messagebox.showerror("Error", "En el modo manual debes \ntraducir todas las palabras.")
                    self.flag_error_manual = True
            else:
                language.make_new_category(category_name=self.in_category.get(),
                                           example=source, automatic_translate=True)

            if not self.flag_error_manual:
                messagebox.showinfo("Correcto", "Tus palabras han sido agregadas :D")
                self.textBox_output.config(state="normal")
                self.textBox_source.delete("1.0", tk.END)
                self.textBox_output.delete("1.0", tk.END)
                self.bt_search.config(state="normal")
                self.bt_save.config(state="disable")
                self.in_category.config(state="normal")
            if self.modes_box.get() == "auto":
                self.textBox_output.config(state="disable")


    def check_for_category(self):
        path = f'languages/{self.languages_box.get()}/{self.in_category.get()}'
        file = Path(path)
        self.textBox_output.config(state="normal")
        if file.is_dir():
            tk.messagebox.showinfo("Correcto", "Esta categoria ya existe. \nSe cargaran los datos anteriores.")
            self.bt_search.config(state="disable")
            self.in_category.config(state="disable")
            self.target_lang = self.languages_box.get().split("_")[0]
            frame = pd.read_csv(f'{path}/{self.in_category.get()}.csv')
            base_words = list(frame['es'])
            target_words = list(frame[self.target_lang])
            self.base_words_loaded = base_words
            self.target_words_loaded = target_words

            base_words = '\n'.join(base_words)
            target_words = '\n'.join(target_words)
            self.textBox_source.insert(tk.END, base_words)
            self.textBox_output.insert(tk.END, target_words)
        else:
            tk.messagebox.showinfo("Correcto", "Esta categoria es completamente nueva")
        self.bt_save.config(state="normal")
        if self.modes_box.get() == "auto":
            self.textBox_output.config(state="disable")


    def language_changed(self, event):
        self.target_lang = self.languages_box.get().split("_")[0]
        self.manual_mode = {"es": ["hola"], self.target_lang: ["hi"]}
        if self.modes_box.get() == "manual":
            self.current_mode = self.manual_mode
        else:
            self.current_mode = self.auto_mode

        self.lb_target_lang = tk.Label(self.inputs_frame, text=self.target_lang)
        self.lb_target_lang.grid(row=0, column=1)



    def mode_changed(self, event):
        if self.modes_box.get() == "manual":
            self.current_mode = self.manual_mode
            self.textBox_output.config(state="normal")
        else:
            self.current_mode = self.auto_mode
            self.textBox_output.config(state="disabled")

    def read_lang_available(self):
        self.languages = self.getDocuments("languages")
        if len(self.languages) == 0:
            self.languages = ['None']

    @staticmethod
    def getDocuments(path):
        objects = [obj.name for obj in Path(path).iterdir()]
        return objects