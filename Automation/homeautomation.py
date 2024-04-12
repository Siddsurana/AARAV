#define BLYNK_TEMPLATE_ID "TMPL3Z40qBBKt"
#define BLYNK_TEMPLATE_NAME "Home Automation"
#define BLYNK_AUTH_TOKEN "iEP3UJIx60wky2bRq_jivwTArC0_gB2Y"

import pyautogui
import webbrowser
import time

def blynk():
    webbrowser.open('https://blynk.cloud/dashboard/login')
    time.sleep(2)
    pyautogui.click(926,879)
blynk()