import pyscreenshot as ImageGrab

# For Full screen
# if __name__ == "__main__":
#     # fullscreen
#     im=ImageGrab.grab()
#     im.show()

if __name__ == "__main__":
    # part of the screen
    im=ImageGrab.grab(bbox=(10,10,510,510)) # X1,Y1,X2,Y2
    im.show()

