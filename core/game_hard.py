from core import Game
from core import VoiceRecognition


class GameHard(Game):
    def __init__(self, lang, category, debug=False):
        super().__init__(lang, category, debug=debug)
        self.vr = VoiceRecognition(lang=self.language.lang)
        self.options = 1

    def make_turn(self, reverse=False):

        source, target, options = self.get_options(reverse)
        self.original_word = source
        self.target_word = target
        if reverse:
            print(f"Traduce de {self.language.lang} a {self.language.base_lang}:")
            self.language.reproduce_text(source)
            self.validate_translate(target, reverse)

        else:
            print(f"Traduce {source} de {self.language.base_lang} a {self.language.lang}:")
            self.validate_translate(target, reverse)
            self.language.reproduce_text(target)

    def validate_translate(self, target, reverse):

        if reverse:  # traducir de otra lengua a español
            source = input()
        else:  # traducir de español a otra lengua (microfono)
            while True:
                source = self.vr.get_text_from_mic()
                print(source)
                ans = input('escribe "a" para aceptar: ')
                if ans == "a":
                    break

        if target == source:
            print("super :D")
            self.points += 1
        else:
            print("que sad :(")
            print("la respuesta correcta es:", target)
            self.corrections[self.original_word] = self.target_word