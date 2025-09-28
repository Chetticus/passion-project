import os    #operating system
import time

import playsound #playsound phat am thanh
import speech_recognition as sr
from gtts import gTTS


SOUND_PATH = "sound.mp3"

def speak(text):
    print(f"Bot: {text}")
    tts = gTTS(text=text, lang="vi", slow=False) #gtts google text to speech
    tts.save(SOUND_PATH)
    playsound.playsound(SOUND_PATH)
    os.remove(SOUND_PATH)

def speak2(text):
    print(f"Bot: {text}")
    tts = gTTS(text=text, lang="vi", slow=True)  # gtts google text to speech
    tts.save(SOUND_PATH)
    playsound.playsound(SOUND_PATH)
    os.remove(SOUND_PATH)
# speak2("Only")
# speak2("Over my dead body")
# speak("I think I killed everybody in the game last year Man, fuck it, I was on though")
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text
        except:
            print("...")
            return ""


while True:
    user_command = ""
    user_command = get_audio()
    if "mở cửa" in user_command:
        speak("Tôi đã mở cửa")
        time.sleep(5)