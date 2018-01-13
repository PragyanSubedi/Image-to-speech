from PIL import Image
import pytesseract
tessdata_dir_config = '--tessdata-dir "/home/pragyan/PycharmProjects/Imagetospeech/tessdata"'
im = Image.open("testimages/nepalitest1.png")

text = pytesseract.image_to_string(im, lang = 'nep', config=tessdata_dir_config)

print(text)