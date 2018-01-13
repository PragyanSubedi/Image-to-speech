from PIL import Image
import pytesseract

im = Image.open("testimages/nepalitest1.png")

text = pytesseract.image_to_string(im, lang = 'nep')

print(text)