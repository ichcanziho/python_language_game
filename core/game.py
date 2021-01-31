from core import LangMaker
from random import randint


class Game:

    def __init__(self, lang, category):

        self.language = LangMaker(lang)
        self.language.set_category(category)
        self.language.load_frame()
        self.points = 0

    def play_rounds(self, rounds):

        for i in range(rounds):
            base_word, translate_word = self.language.make_random_pair()
            if randint(0, 1):
                print(f'Traduce {base_word} de {self.language.base_lang} a {self.language.lang}:',)
                answer = input()
                if answer == translate_word:
                    self.points += 1
                    print("Muy bien :D")
                    self.language.reproduce_text(translate_word)
                else:
                    print(":( la respuesta correcta era:", translate_word)
                    self.language.reproduce_text(translate_word)

            else:
                self.language.reproduce_text(translate_word)
                print(f'Traduce {translate_word} de {self.language.lang} a {self.language.base_lang}')

                answer = input()
                if answer == base_word:
                    self.points += 1
                    print("Muy bien :D")
                else:
                    print(":( la respuesta correcta era:", base_word)
