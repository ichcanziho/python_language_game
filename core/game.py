from core import LangMaker
from random import choice, randint, shuffle


class Game:

    def __init__(self, lang, category, debug=False):

        self.language = LangMaker(lang)
        self.language.set_category(category)
        self.language.load_frame(debug)
        if debug:
            print("category size:", len(self.language.frame))
        self.points = 0
        self.options = 1
        self.rounds = 1
        self.corrections = dict()
        self.original_word = ""
        self.target_word = ""

    def make_turn(self, reverse=False):
        pass

    def show_score(self):
        print(f'Tuviste {self.points}/{self.rounds} | {self.points/self.rounds * 100}%')
        if self.points != self.rounds:
            print("repasa las siguientes parejas:")
            for key, value in self.corrections.items():
                print(key, value)
        else:
            print("felicidades tuviste todas bien, continua así.")

    def play_rounds(self, rounds):
        self.rounds = rounds
        for _ in range(rounds):
            self.make_turn(choice([True, False]))

        self.show_score()

    def get_options(self, reverse=False):

        limit = len(self.language.frame)
        random_index = []
        while True:
            selection = randint(0, limit-1)
            if selection not in random_index:
                random_index.append(selection)

            if len(random_index) == self.options:
                break

        base_words_dict, translate_words_dict = self.language.make_random_pairs(random_index)
        key_base_words = list(base_words_dict.keys())
        key_translate_words = list(translate_words_dict.keys())
        base_word = key_base_words[0]
        translate_word = base_words_dict.get(base_word)
        shuffle(key_base_words)
        shuffle(key_translate_words)

        if reverse:
            return translate_word, base_word, key_base_words
        else:
            return base_word, translate_word, key_translate_words



