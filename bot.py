from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

class Coordinates():
    restart=(1025,383)
    dino =(850,385)

def restartGame() :
    pyautogui.click(Coordinates.restart)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
    pyautogui.keyUp('space')
    
def imageGrab():
    # box = ( Coordinates.dino[0]+7,Coordinates.dino[1]+7,Coordinates.dino[0]+30,Coordinates.dino[1]+35)
    box=(857,381,880,415)
    image =ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a= array(grayImage.getcolors())
    print (a.sum())
    return a.sum()

def main() :
    restartGame()    

    while True:
        if(imageGrab() > 1029):
            pressSpace()

main()