import webbrowser
import time
import pyautogui

def start_gpt_prompt(query):
    
    webbrowser.open("https://chat.openai.com")

    time.sleep(5) 
 
    pyautogui.click(x=500, y=900) 

    pyautogui.typewrite(query)

    pyautogui.press("enter")

