from core import T2S
from pathlib import Path
import pandas as pd
from random import randint


class LangMaker(T2S):

    def __init__(self, lang_folder, base_lang="es"):
        self.base_lang = base_lang
        super().__init__(lang=lang_folder)
        self.frame = None

    def load_frame(self):
        cate = self.root_category
        if cate is None:
            assert ValueError("you must specify a category before load a frame")
        self.frame = pd.read_csv(f'{cate}/{cate.split("/")[-1]}.csv')

    def make_new_category(self, category_name, example=None) -> None:
        """
        creates a new folder structure for a given language
        :param category_name: the name of the new category to be created
        :param example: you can give a list of words and their translate
        :return: None
        """
        if not (Path(f'{self.lang_folder}/{category_name}').is_dir()):
            Path.mkdir(Path(f'{self.lang_folder}/{category_name}'))
            Path.mkdir(Path(f'{self.lang_folder}/{category_name}/sounds'))
            if example is None:
                frame = pd.DataFrame({self.base_lang: [],
                                      self.lang: []})
                frame.to_csv(f'{self.lang_folder}/{category_name}/{category_name}.csv', index=False)
            else:
                example = list(zip(*example))
                original_words = example[0]
                translate_words = example[1]
                frame = pd.DataFrame({self.base_lang: original_words,
                                      self.lang: translate_words})
                frame.to_csv(f'{self.lang_folder}/{category_name}/{category_name}.csv', index=False)

                self.set_category(category_name)
                for word in translate_words:
                    self.text_to_mp3(word)

        else:
            print("Category:", category_name, "already exists")

    def translate_word(self, word, reverse=False):
        if self.frame is None:
            assert ValueError("you must load a frame before translate a word")

        if not reverse:
            try:
                row = self.frame.loc[self.frame[self.base_lang] == word]
                translate = str(row[self.lang].values[0])
                print(translate)
            except IndexError:
                print(word, "is not in the database")

        else:
            row = self.frame.loc[self.frame[self.lang] == word]
            translate = str(row[self.base_lang].values[0])
            print(translate)

    def make_random_pair(self):
        if self.frame is None:
            assert ValueError("you must load a frame before translate a word")

        random_index = randint(0, len(self.frame)-1)
        row = self.frame.iloc[random_index]
        base_word = row[self.base_lang]
        translate_word = row[self.lang]
        return base_word, translate_word





