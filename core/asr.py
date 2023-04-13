import speech_recognition as sr
import pyaudio
import os
r = sr.Recognizer()
path ="/home/manhd/django-ajax-record/media/records/"
# k = path+'audiorecord.wav'
def stt(k):
    

    with sr.AudioFile(k) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio,language="vi-VI")
        return text
    except:
        print("Xin lỗi! tôi không nhận được voice!")

        