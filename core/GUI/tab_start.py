from tkinter import ttk
import tkinter as tk
from pathlib import Path
import json
from core.GUI.win_medium import WindowMedium
from core.GUI.win_hard import WindowHard
from core.GUI.win_easy import WindowEasy


class TabPlay:

    def __init__(self, nb):
        self.nb = nb
        self.window = ttk.Frame(self.nb)
        file = Path("./settings.json")
        if not file.is_file():
            self.set_default_settings()

        with open("settings.json") as json_file:
            self.current_settings = json.load(json_file)

        self.bt_play = None
        self.make_start_button()

        self.nb.add(self.window, text='Play')

    def make_start_button(self):
        self.bt_play = tk.Button(self.window, text="Jugar",
                                 command=self.open_game_window,
                                 padx=50, pady=50, bg="bisque")
        self.bt_play.pack(pady=50)

    def open_game_window(self):
        with open("settings.json") as json_file:
            self.current_settings = json.load(json_file)
        window_game = tk.Tk()
        if self.current_settings["difficulty"] == "med":
            game = WindowMedium(window_game, **self.current_settings)
        elif self.current_settings["difficulty"] == "hard":
            game = WindowHard(window_game, **self.current_settings)
        else:
            game = WindowEasy(window_game, **self.current_settings)
        game.mainloop()

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
