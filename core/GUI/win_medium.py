import tkinter as tk
from tkinter import messagebox
from core.GUI.win_base import WindowBase


class WindowMedium(WindowBase):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.make_sentence_label()
        self.update_sentence()
        self.make_ans_input()
        self.make_send_button()
        self.make_turns_label()
        self.update_turns_passed()
        self.make_hint_label()
        self.update_hint(":)")

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
                self.update_hint(":)")
                self.bt_play.config(state="normal")
                self.master.lift()
            else:
                self.master.destroy()
        else:
            self.update_sentence()
