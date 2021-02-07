import tkinter as tk
from random import choice
from core import GameNormal
from core import GameHard
from core import GameEasy


class WindowBase(tk.Frame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master)

        self.ans_error_path = "others/sounds/error.mp3"
        self.ans_correct_path = "others/sounds/correct.mp3"
        self.master.title(f"Dificultad {kwargs['difficulty']}")
        self.master.geometry('300x250')
        self.target_lang = kwargs["target_lang"]
        self.category = kwargs["category"]
        self.rounds = int(kwargs['questions'])

        if kwargs['difficulty'] == "med":
            self.game = GameNormal(lang=self.target_lang, category=self.category)
        elif kwargs['difficulty'] == "hard":
            self.game = GameHard(lang=self.target_lang, category=self.category)
        else:
            self.game = GameEasy(lang=self.target_lang, category=self.category)

        self.turns_played = 0
        self.button_flag = True
        self.master.bind("<Return>", self.send_button_action)

    def make_sentence_label(self):
        self.sentence_var = tk.StringVar(self.master)
        self.lb_sentence = tk.Label(self.master, textvariable=self.sentence_var)
        self.lb_sentence.pack(pady=20)

    def make_ans_input(self):
        self.in_answer = tk.Entry(self.master, width=22)
        self.in_answer.pack()

    def make_send_button(self):
        self.bt_play = tk.Button(self.master, text="Probar",
                                 command=self.send_button_action,
                                 padx=20, pady=15, bg="bisque")
        self.bt_play.pack(pady=20)

    def make_turns_label(self):
        self.turns_passed = tk.StringVar(self.master)
        self.lb_turns = tk.Label(self.master, textvariable=self.turns_passed)
        self.lb_turns.pack(pady=10)

    def make_hint_label(self):
        self.hint_var = tk.StringVar(self.master)
        self.lb_hint = tk.Label(self.master, textvariable=self.hint_var)
        self.lb_hint.pack()

    def update_hint(self, hint):
        self.hint_var.set(hint)
        self.lb_hint.config(textvariable=self.hint_var)

    def update_turns_passed(self):
        sentence = f'{self.turns_played}/{self.rounds}'
        self.turns_passed.set(sentence)
        self.lb_turns.config(textvariable=self.turns_passed)

    def update_sentence(self, aux=False):
        reverse = choice([True, False])
        self.reverse_option = reverse
        self.source, self.target, self.options = self.game.get_options(reverse=reverse)
        if reverse:
            if aux:
                sentence = f"Traduce de {self.game.language.lang} a {self.game.language.base_lang}:"
            else:
                sentence = f"Traduce {self.source} de {self.game.language.lang} a {self.game.language.base_lang}:"
            self.game.language.reproduce_text(self.source)
        else:
            sentence = f"Traduce {self.source} de {self.game.language.base_lang} a {self.game.language.lang}:"

        self.sentence_var.set(sentence)
        self.lb_sentence.config(textvariable=self.sentence_var)

    def send_button_action(self, event=None):
        print("picaste el boton probar")

    def verify_answer(self):
        print("intentas verificar la respuesta")

    def verify_game_ends(self):
        print("intentas verificar que el juego halla terminado")
