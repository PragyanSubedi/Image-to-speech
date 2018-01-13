from PIL import Image
import pytesseract

im = Image.open("test2.png")

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)