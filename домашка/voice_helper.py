#
# import speech_recognition as sr
#
# recognizer = sr.Recognizer()
#
# while True:
#     with sr.Microphone(device_index=1) as source:
#         print("Скажите что-нибудь...")
#
#         speech = recognizer.listen(source)
#
#         speech_to_text = recognizer.recognize_google(speech, language="ru_RU").lower()
#
#         print(f"Вы сказали: {speech_to_text}")
#
# hello = ["привет", "здравствуйте", "приветик"]
# f = open("test.txt", "r", encoding="utf-8")
# f.write(speech_to_text)
# random_hello = random.choice(hello)
# f.close()


from pygame import mixer, time
from gtts import gTTS
import speech_recognition as sr
import random

r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    print("listening")
    audio = r.listen(source)

speech = r.recognize_google(audio, language="ru-RU").lower()
print("Вы сказали:", speech)

hello = ["привет", "приветствую", "ку", "здарова", "рад вас видеть", "приветик"]

file_my = open("chgk\my_file.txt", "w", encoding="utf")
file_my.write(speech)

rand_hello = random.choice(hello)

if speech == "привет":
    mixer.init()
    tts = gTTS(text=rand_hello, lang="ru")
    tts.save("chgk\\aud.mp3")
    mixer.music.load("chgk\\aud.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play()
    print("Бот: ", rand_hello)
    time.wait(10000)

file_my.close()