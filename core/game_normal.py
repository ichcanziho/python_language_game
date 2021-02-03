from core import Game


class GameNormal(Game):
    def __init__(self, lang, category, debug=False):
        super().__init__(lang, category, debug=debug)
        self.options = 1

    def make_turn(self, reverse=False):

        source, target, options = self.get_options(reverse)
        self.original_word = source
        self.target_word = target
        if reverse:
            print(f"Traduce {source} de {self.language.lang} a {self.language.base_lang}:")
            self.language.reproduce_text(source)
            self.validate_translate(target)

        else:
            print(f"Traduce {source} de {self.language.base_lang} a {self.language.lang}:")
            self.validate_translate(target)
            self.language.reproduce_text(target)

    def validate_translate(self, target):
        source = input()
        if target == source:
            print("super :D")
            self.points += 1
        else:
            print("que sad :(")
            print("la respuesta correcta es:", target)
            self.corrections[self.original_word] = self.target_word


