from random import choice, randint, shuffle
from core import Game


class GameEasy(Game):
    def __init__(self, lang, category, debug=False):
        super().__init__(lang, category, debug=debug)
        self.options = 4

    def make_turn(self, reverse=False):

        source, target, options = self.get_options(reverse)
        self.original_word = source
        self.target_word = target
        if reverse:

            print(f"Traduce {source} de {self.language.lang} a {self.language.base_lang}:")
            self.language.reproduce_text(source)
            self.show_options(options)
            option = self.validate_option()
            self.validate_translate(target, options, option)

        else:
            print(f"Traduce {source} de {self.language.base_lang} a {self.language.lang}:")
            self.show_options(options)
            option = self.validate_option()
            self.validate_translate(target, options, option)
            self.language.reproduce_text(options[option])

    def validate_translate(self, target, options, option):
        if target == options[option]:
            print("super :D")
            self.points += 1
        else:
            self.corrections[self.original_word] = self.target_word
            print("que sad :(")
            print("la respuesta correcta es:", target)

    @staticmethod
    def show_options(options):
        print("Selecciona un número:")
        for i, option in enumerate(options, 1):
            print(f'{i}: {option}')

    @staticmethod
    def validate_option():

        while True:
            print("------")
            n = input()
            if n.isnumeric() and n in ["1", "2", "3", "4"]:
                return int(n) - 1
            else:
                print(n, "no es una opción válida")



