import tkinter as tk
from tkinter import messagebox
from core.GUI.win_base import WindowBase
from playsound import playsound


class WindowEasy(WindowBase):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bt_option_1 = None
        self.bt_option_2 = None
        self.bt_option_3 = None
        self.bt_option_4 = None
        self.word_choice = None
        self.make_sentence_label()
        self.update_sentence()
        self.make_answer_buttons()
        self.update_answer_buttons_labels()
        self.make_turns_label()
        self.update_turns_passed()
        self.make_hint_label()
        self.update_hint(":)")
        self.master.bind("1", self.one_key_clicked)
        self.master.bind("2", self.two_key_clicked)
        self.master.bind("3", self.three_key_clicked)
        self.master.bind("4", self.four_key_clicked)

    def one_key_clicked(self, event):
        self.action_button_clicked(0)

    def two_key_clicked(self, event):
        self.action_button_clicked(1)

    def three_key_clicked(self, event):
        self.action_button_clicked(2)

    def four_key_clicked(self, event):
        self.action_button_clicked(3)

    def make_answer_buttons(self):
        auxFrame1 = tk.Frame(self.master)
        auxFrame1.pack(pady=10)
        self.bt_option_1 = tk.Button(auxFrame1, text="1", width=16, height=2, bg="bisque",
                                     command=lambda: self.action_button_clicked(0))
        self.bt_option_1.pack(side=tk.LEFT, padx=5)
        self.bt_option_2 = tk.Button(auxFrame1, text="2", width=16, height=2, bg="bisque",
                                     command=lambda: self.action_button_clicked(1))
        self.bt_option_2.pack(side=tk.LEFT, padx=5)
        auxFrame2 = tk.Frame(self.master)
        auxFrame2.pack(pady=10)
        self.bt_option_3 = tk.Button(auxFrame2, text="3", width=16, height=2, bg="bisque",
                                     command=lambda: self.action_button_clicked(2))
        self.bt_option_3.pack(side=tk.LEFT, padx=5)
        self.bt_option_4 = tk.Button(auxFrame2, text="4", width=16, height=2, bg="bisque",
                                     command=lambda: self.action_button_clicked(3))
        self.bt_option_4.pack(side=tk.LEFT, padx=5)

    def update_answer_buttons_labels(self):
        self.bt_option_1.config(text=f'1: {self.options[0]}')
        self.bt_option_2.config(text=f'2: {self.options[1]}')
        self.bt_option_3.config(text=f'3: {self.options[2]}')
        self.bt_option_4.config(text=f'4: {self.options[3]}')

    def action_button_clicked(self, number):
        if self.button_flag and number != -1:
            self.word_choice = self.options[number]
            self.turns_played += 1
            self.verify_answer()
            self.button_flag = False
            self.bt_option_1.config(text=f'continuar', bg="turquoise")
            self.bt_option_2.config(text=f'continuar', bg="turquoise")
            self.bt_option_3.config(text=f'continuar', bg="turquoise")
            self.bt_option_4.config(text=f'continuar', bg="turquoise")
            self.update_turns_passed()
        else:
            self.bt_option_1.config(bg="bisque")
            self.bt_option_2.config(bg="bisque")
            self.bt_option_3.config(bg="bisque")
            self.bt_option_4.config(bg="bisque")
            self.button_flag = True
            self.update_hint(":)")
            self.verify_game_ends()

    def send_button_action(self, event=None):
        if not self.button_flag:
            self.action_button_clicked(-1)

    def verify_answer(self):
        if self.word_choice == self.target:
            self.game.points += 1
            self.update_hint("correcto :D")
            playsound(self.ans_correct_path)
        else:
            self.update_hint(f'{self.source} es {self.target}')
            playsound(self.ans_error_path)
        if not self.reverse_option:
            self.game.language.reproduce_text(self.target)

    def verify_game_ends(self):

        if self.turns_played == self.rounds:
            points = round(self.game.points/self.rounds, 2)*100
            ans = tk.messagebox.askyesno("Terminaste", f"Tu puntuacion fue: {points}\n¿volver a jugar?")
            if ans:
                self.game.points = 0
                self.turns_played = 0
                self.update_turns_passed()
                self.update_sentence()
                self.update_answer_buttons_labels()
                self.update_hint(":)")
                self.master.lift()
            else:
                self.master.destroy()
        else:
            self.update_sentence()
            self.update_answer_buttons_labels()
