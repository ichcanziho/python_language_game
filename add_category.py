from core import LangMaker


def manual_translate():
    language = LangMaker("en_English")
    language.make_new_category(category_name="colors",
                               example=[
                                   ["rojo", "red"],
                                   ["azul", "blue"],
                                   ["amarillo", "yellow"]
                               ])


def automatic_translate():
    language = LangMaker("en_English")
    language.make_new_category(category_name="animals",
                               example=["perro", "gato", "tigre", "tortuga", "sapo", "rana"],
                               automatic_translate=True)


def main(method):

    if method == "manual":
        manual_translate()
    elif method == "auto":
        automatic_translate()
    else:
        print("we can't find that method")


if __name__ == "__main__":
    main("auto")



