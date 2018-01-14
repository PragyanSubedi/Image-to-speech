from PIL import Image
import pytesseract
tessdata_dir_config = '--tessdata-dir "/home/pragyan/PycharmProjects/Imagetospeech/tessdata"'
im = Image.open("testimages/test3.png")

text = pytesseract.image_to_string(im, lang = 'UbuntuR', config=tessdata_dir_config)

print(text)