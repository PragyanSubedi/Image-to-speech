import pyttsx3

k = pyttsx3.init()

def say(text):
    k.say(text)
    k.runAndWait()

say('Hi I am human.')