import whisper
import pyttsx3

class VoiceAgent:
    def __init__(self):
        self.stt_model = whisper.load_model("base")  # Whisper model for STT
        self.tts_engine = pyttsx3.init()  # TTS engine

    def stt(self, audio_file):
        result = self.stt_model.transcribe(audio_file)
        return result['text']

    def tts(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
