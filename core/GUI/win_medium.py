import tkinter as tk
from core import GameNormal
from random import choice
from tkinter import messagebox
from time import sleep

class WindowMedium(tk.Frame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master)
        self.master.title("Dificultad Media")
        self.master.geometry('300x250')
        self.target_lang = kwargs["target_lang"]
        self.category = kwargs["category"]
        self.rounds = int(kwargs['questions'])

        self.master.bind("<Return>", self.send_button_action)

        print(self.target_lang, end=" ")
        print(self.category, end=" ")
        print(self.rounds)
        self.turns_played = 0
        self.game = GameNormal(lang=self.target_lang,
                               category=self.category)
        self.sentence_var = tk.StringVar(self.master)
        self.turns_passed = tk.StringVar(self.master)

        self.make_sentence_label()
        self.update_sentence()
        self.make_ans_input()
        self.make_send_button()
        self.make_points_label()
        self.update_turns_passed()

    def update_sentence(self):
        reverse = choice([True, False])
        self.reverse_option = reverse
        self.source, self.target, self.options = self.game.get_options(reverse=reverse)
        if reverse:
            sentence = f"Traduce {self.source} de {self.game.language.lang} a {self.game.language.base_lang}:"
            self.game.language.reproduce_text(self.source)
        else:
            sentence = f"Traduce {self.source} de {self.game.language.base_lang} a {self.game.language.lang}:"

        self.sentence_var.set(sentence)
        self.lb_sentence.config(textvariable=self.sentence_var)

    def update_turns_passed(self):
        sentence = f'{self.turns_played}/{self.rounds}'
        self.turns_passed.set(sentence)
        self.lb_turns.config(textvariable=self.turns_passed)

    def make_sentence_label(self):
        self.lb_sentence = tk.Label(self.master, textvariable=self.sentence_var)
        self.lb_sentence.pack(pady=30)

    def make_ans_input(self):
        self.in_answer = tk.Entry(self.master, width=22)
        self.in_answer.pack()

    def make_send_button(self):
        self.bt_play = tk.Button(self.master, text="Probar",
                                 command=self.send_button_action,
                                 padx=20, pady=15, bg="bisque")
        self.bt_play.pack(pady=20)

    def make_points_label(self):
        self.lb_turns = tk.Label(self.master, textvariable=self.turns_passed)
        self.lb_turns.pack(pady=15)

    def send_button_action(self, event=None):
        self.turns_played += 1
        self.verify_answer()
        self.in_answer.delete("0", tk.END)
        self.update_turns_passed()
        self.verify_game_ends()



    def verify_answer(self):
        if self.in_answer.get() == self.target:
            self.game.points += 1
        if not self.reverse_option:
            self.game.language.reproduce_text(self.target)
            sleep(1)

        print("tu", self.in_answer.get())
        print("ans", self.target)
        print(self.game.points)

    def verify_game_ends(self):
        if self.turns_played == self.rounds:
            self.bt_play.config(state="disable")
            points = round(self.game.points/self.rounds, 2)*100
            ans = tk.messagebox.askyesno("Terminaste", f"Tu puntuacion fue: {points}\n¿volver a jugar?")
            if ans:
                self.game.points = 0
                self.turns_played = 0
                self.update_turns_passed()
                self.update_sentence()
                self.bt_play.config(state="normal")
                self.master.lift()
            else:
                self.master.destroy()
        else:
            self.update_sentence()

