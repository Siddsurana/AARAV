import webbrowser
import time
import pyautogui

def onlight1():
    webbrowser.open('https://web.telegram.org/k/#@control1209bot', new=2)
    time.sleep(3)
    pyautogui.click(1584, 1819)
    time.sleep(1)
    pyautogui.write("Light laga")
    time.sleep(1)
    pyautogui.press('enter')

def onlight2():
    webbrowser.open('https://web.telegram.org/k/#@control1209bot', new=2)
    time.sleep(3)
    pyautogui.click(1584, 1819)
    pyautogui.write("Dusra Light Laga")

def onfan():
    webbrowser.open('https://web.telegram.org/k/#@control1209bot', new=2)
    time.sleep(3)
    pyautogui.click(1584, 1819)
    pyautogui.write("Fan laga bhai")

def offlight1():
    webbrowser.open('https://web.telegram.org/k/#@control1209bot', new=2)
    time.sleep(3)
    pyautogui.click(1584, 1819)
    time.sleep(1)
    pyautogui.write("Light band kar")

def offlight2():
    webbrowser.open('https://web.telegram.org/k/#@control1209bot', new=2)
    time.sleep(3)
    pyautogui.click(1584, 1819)
    pyautogui.write("Dusra light band kar")

def offfan():
    webbrowser.open('https://web.telegram.org/k/#@control1209bot', new=2)
    time.sleep(3)
    pyautogui.click(1584, 1819)
    pyautogui.write("Fan band kar")







