import tkinter as tk
from tkinter import messagebox
from playsound import playsound
from core.GUI.win_base import WindowBase
from core import VoiceRecognition


class WindowHard(WindowBase):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.vr = VoiceRecognition(lang=self.game.language.lang)
        self.master.geometry('300x300')
        self.make_sentence_label()
        self.update_sentence(aux=True)
        self.make_ans_input()
        self.make_option_buttons()
        self.update_options_buttons()
        self.make_send_button()
        self.make_turns_label()
        self.update_turns_passed()
        self.make_hint_label()
        self.update_hint(":)")

    def make_option_buttons(self):
        auxFrame = tk.Frame(self.master)
        auxFrame.pack(pady=15)
        self.bt_play_word = tk.Button(auxFrame, text="Reproducir", width=12, bg="linen",
                                      command=self.action_play_word)
        self.bt_play_word.pack(side=tk.LEFT, padx=5)
        self.bt_lisent = tk.Button(auxFrame, text="Hablar", width=12, bg="PaleTurquoise1",
                                   command=self.action_bt_lisent)
        self.bt_lisent.pack(side=tk.LEFT, padx=5)

    def update_options_buttons(self):
        if self.reverse_option:
            self.bt_lisent.config(state="disable")
            self.bt_play_word.config(state="normal")
            self.in_answer.config(state="normal")
        else:
            self.bt_lisent.config(state="normal")
            self.bt_play_word.config(state="disable")
            self.in_answer.config(state="disable")

    def action_play_word(self):
        self.game.language.reproduce_text(self.source)

    def action_bt_lisent(self):
        self.in_answer.config(state="normal")
        self.in_answer.delete(0, "end")
        self.in_answer.config(state="disable")
        source = self.vr.get_text_from_mic()
        self.in_answer.config(state="normal")
        self.in_answer.insert(0, source)
        self.in_answer.config(state="disable")
        print(source)


    def send_button_action(self, event=None):

        if self.button_flag:
            self.turns_played += 1
            self.verify_answer()
            self.in_answer.delete("0", tk.END)

            self.bt_play.config(text="Continuar", bg="turquoise")
            self.button_flag = False
            self.in_answer.config(state="disable")
        else:
            self.button_flag = True

            self.in_answer.config(state="normal")
            self.bt_play.config(text="Probar", bg="bisque")
            self.update_hint(":)")
            self.update_turns_passed()
            self.verify_game_ends()

    def verify_answer(self):
        if self.in_answer.get() == self.target:
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
            self.bt_play.config(state="disable")
            points = round(self.game.points/self.rounds, 2)*100
            ans = tk.messagebox.askyesno("Terminaste", f"Tu puntuacion fue: {points}\n¿volver a jugar?")
            if ans:
                self.game.points = 0
                self.turns_played = 0
                self.update_turns_passed()
                self.in_answer.config(state="normal")
                self.in_answer.delete(0, "end")
                self.update_sentence(aux=True)
                self.update_options_buttons()
                self.update_hint(":)")
                self.bt_play.config(state="normal")
                self.master.lift()
            else:
                self.master.destroy()
        else:
            self.in_answer.config(state="normal")
            self.in_answer.delete(0, "end")
            self.update_sentence(aux=True)
            self.update_options_buttons()