#Replacing PIL.ImageGrab for Ubuntu 16.04
import pyscreenshot as ImageGrab
import Tkinter
# import pytesseract
# from PIL import Image

root = Tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# For Full screen
# if __name__ == "__main__":
#     # fullscreen
#     im=ImageGrab.grab()
#     im.show()

# if __name__ == "__main__":
    # part of the screen
im=ImageGrab.grab(bbox=(200,200,600,600)) # X1,Y1,X2,Y2
im.show()

