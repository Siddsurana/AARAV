import webbrowser
import time
import pyautogui

def onlight1():
    webbrowser.open('https://web.telegram.org/k/#@control1209bot', new=2)
    time.sleep(3)
    pyautogui.click(1584, 1819)
    time.sleep(1)
    pyautogui.write("Switch on the bulb")
    time.sleep(1)
    pyautogui.press('enter')



def onfan():
    webbrowser.open('https://web.telegram.org/k/#@control1209bot', new=2)
    time.sleep(3)
    pyautogui.click(1584, 1819)
    pyautogui.write("Switch on the fan")

def offlight1():
    webbrowser.open('https://web.telegram.org/k/#@control1209bot', new=2)
    time.sleep(3)
    pyautogui.click(1584, 1819)
    time.sleep(1)
    pyautogui.write("Turn off the bulb")


def offfan():
    webbrowser.open('https://web.telegram.org/k/#@control1209bot', new=2)
    time.sleep(3)
    pyautogui.click(1584, 1819)
    pyautogui.write("Turn off the fan")







