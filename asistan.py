from asyncore import write
from cProfile import run
from distutils.text_file import TextFile
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import date, datetime
import random
from random import choice
import webbrowser
import psutil
from plyer import notification
import time
import pywhatkit as k
import pyttsx3


r = sr.Recognizer()

engine = pyttsx3.init()
engine.say("Seni tekrardan görmek güzel")
engine.runAndWait()

def record(ask=False):
    playsound("DING.mp3")
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.RequestError:
            speak("Sistem çalışmıyor")
        return voice
    
    
def ingrecord(ask=False):
    playsound(r"C:\Users\hakan\Desktop\nly dg\DING.mp3")
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="en-EN")
        except sr.UnknownValueError:
            speak("Anlayamadım")
        except sr.RequestError:
            speak("Sistem çalışmıyor")
        return voice


# ana komutlar
def response(voice):
    if "merhaba" in voice:
        speak("Merhaba sana nasıl yardımcı olabilirim.?")
    if "beni duyuyor musun" in voice:
        speak("Evet duyuyorum")
    if "ne" in voice:
        speak("Anlamadım")
    if "nasılsın" in voice:
        speak("iyiyim sen nasılsın")
    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("rica ederim bunun için buradayım")
    if "bu gün nasılsın" in voice:
        speak("İyiyim teşekkürler sen nasılsın?")
    if "iyiyim" in voice:
        speak("Hep iyi ol")
    if "kötüyüm" in voice:
        speak("Buna üzüldüm senin için yapabilecğim bir şey varmı")
        if "hayır" in voice:
            speak("Peki")
        if "evet" in voice:
            speak("Yardıma ihtiyacı varsa yanındayım.")   
    if "en sevdiğim renk ne" in voice or "renk" in voice:
        speak("mor") 
    if "görüşürüz" in voice or "bay bay" in voice or "kapan" in voice or "baybay" in voice:
        speak("görüşürüz ")
        exit()
        
#genel komutlar

    if "not al" in voice:
        speak("Dosya ismi ne olsun")
        txtFile = record() + ".txt"
        speak("Ne kaydetmek istiyorsun")
        theText = record()
        f = open(txtFile, "w", encoding="utf-8")
        f.writelines(theText)
        f.close()

    if "hangi gündeyiz" in voice or "günlerden ne" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wednesday":
            today = "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"

        elif today == "Saturday":
            today = "Cumartesi"

        elif today == "Sunday":
            today = "Pazar"

        speak(today)

    if "saat kaç" in voice:
        clock = datetime.now().strftime("%H:%M")
        speak(clock)

    if "bilgisayarı yeniden başlat" in voice or "bilgisayar yeniden başlat" in voice or "pc reset" in voice:
        speak("Bilgisayarı yeniden başlatma mı ister misin?")
        onay = record()
        onay = onay.lower()
        if "evet" in onay:
            speak("Sistem yeniden başlatılıyor")
            os.system("shutdown /r /t 2")
            os.system("TASKKILL /F /IM Asistan.exe")
        if "hayır" in onay:
            speak("İşlem iptal edildi")  

    if "bilgisayarı kapat" in voice or "bilgisayar kapat" in voice or "pc stop" in voice:
        speak("Bilgisayarı kapatmamı ister misin?")
        onay = record()
        onay = onay.lower()
        if "evet" in onay:
            speak("Sistem kapatılıyor")
            os.system("shutdown /s /t 5")
            os.system("TASKKILL /F /IM Asistan.exe")
        if "hayır" in onay:
            speak("İşlem iptal edildi")


    if "google" in voice:
        speak("Googleda ne aramamı istersin?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("İşte google sonuçları")

    if "youtube" in voice:
        speak("Ne izlemek istersin?")
        search = record()
        url = "https://www.youtube.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("İyi izlemeler :)")

    if "müzik aç" in voice:
        speak("Ne dinlemek istersin?")
        search = record()
        url = "https://music.youtube.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("İyi Dinlemeler")

    if "uygulama aç" in voice:
        speak("Hangi uygulamayı açmamı istiyorsun?")
        runApp = record()
        runApp = runApp.lower()
        if "google" in  runApp:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            speak("google açtım.")
            os.system("TASKKILL /F /IM Asistan.exe")
        else:
            speak("İstediğin uygulama çalıştırma listemde yok.")

def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

while True:
    wake = record()
    if wake != '':
       wake = wake.lower()
       print(wake)
       response(wake)