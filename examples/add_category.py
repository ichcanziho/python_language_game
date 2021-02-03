from core import LangMaker
import os

os.chdir("..")


def create_empty_category(lang, category):

    language = LangMaker(lang_folder=lang)
    language.make_new_category(category_name=category)


def create_manual_category(lang, category, words):
    language = LangMaker(lang_folder=lang)
    language.make_new_category(category_name=category, example=words)


def create_automatic_category(lang, category, words):
    language = LangMaker(lang_folder=lang)
    language.make_new_category(category_name=category, example=words, automatic_translate=True)


def main(selector):
    if selector == "e":
        create_empty_category("fr_French", "test")
    elif selector == "m":
        create_manual_category("fr_French", "animales", [["animal", "animal"],
                                                     ["gato", "chat"]
                                                     ])
    elif selector == "a":
        create_automatic_category("fr_French", "test", ["chico", "chica"])


if __name__ == "__main__":
    main("m")


