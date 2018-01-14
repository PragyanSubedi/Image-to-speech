from PIL import Image
import pytesseract
import pyttsx3
import pyscreenshot as ImageGrab

# Image to speech conversion
tessdata_dir_config = '--tessdata-dir "/home/pragyan/PycharmProjects/Imagetospeech/tessdata"'
im = Image.open("testimages/test3.png")

text = pytesseract.image_to_string(im, lang = 'UbuntuR', config=tessdata_dir_config)

print(text)


k = pyttsx3.init()

def say(text):
    k.say(text)
    k.runAndWait()

say(text)