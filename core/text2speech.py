from gtts import gTTS
from playsound import playsound
from pathlib import Path
import unidecode


class T2S:

    def __init__(self, lang):
        self.lang_folder = f'languages/{lang}'
        self.lang = lang.split("_")[0]
        self.root_category = None

    def set_category(self, category):
        self.root_category = f'{self.lang_folder}/{category}'

    def reproduce_text(self, text="hello", slow=False):
        if self.root_category is None:
            raise ValueError("You must specify a category before reproduce a text ")

        if not (Path(f'{self.root_category}/sounds').is_dir()):
            Path.mkdir(Path(f'{self.root_category}/sounds'))

        path = self.text_to_mp3(text=text, slow=slow)
        playsound(path)

    def text_to_mp3(self, text, slow=False, alarm=False):
        tts = gTTS(text, lang=self.lang, slow=slow)
        text = unidecode.unidecode(text)
        path = f'{self.root_category}/sounds/{text}.mp3'
        file = Path(path)
        if not (file.is_file()):
            tts.save(path)
            if alarm:
                print("Writing:", text, "| in sounds folder")
        else:
            if alarm:
                print(text, "already exists")
        return path


if __name__ == "__main__":
    french = T2S(lang="fr")
    french.reproduce_text(text="le chat est noir")










