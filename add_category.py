from core import LangMaker


def main():

    language = LangMaker("en_English")
    language.make_new_category(category_name="colors",
                               example=[
                                   ["rojo", "red"],
                                   ["azul", "blue"],
                                   ["amarillo", "yellow"]
                               ])


if __name__ == "__main__":
    main()
