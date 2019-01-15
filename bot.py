from PIL import ImageGrab
import pyautogui

class Coordinates():
    restart=(1025,383)

def restartGame() :
    pyautogui.click(Coordinates.restart)

restartGame()    