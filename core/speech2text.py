import speech_recognition as sr


class VoiceRecognition:

    def __init__(self, lang):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()  # Microphone.list_microphone_names()
        if lang == "fr":
            lang = "fr-FR"
        self.lang = lang

    def get_text_from_mic(self):

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        response = {
                "success": True,
                "error": None,
                "transcription": None
                }
        try:
            response["transcription"] = self.recognizer.recognize_google(audio, language=self.lang)
        except sr.RequestError:
            response["success"] = False
            response["error"] = "API unavailable"
            return "API error"
        except sr.UnknownValueError:
            response["error"] = "Unable to recognize speech"
            return "repeat please"

        return response["transcription"]
