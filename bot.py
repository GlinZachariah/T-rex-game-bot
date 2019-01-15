from PIL import ImageGrab
import pyautogui
import time

class Coordinates():
    restart=(1025,383)
    dino =(850,390)

def restartGame() :
    pyautogui.click(Coordinates.restart)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
    pyautogui.keyUp('space')
    
restartGame()    
time.sleep(1)
pressSpace()