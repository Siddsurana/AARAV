
import pyautogui
from threading import Thread

class ScrollControl(Thread):
    def __init__(self):
        super().__init__()
        self.running_up = False
        self.running_down = False

    def run(self):
        while True:
            if self.running_up:
                pyautogui.scroll(10)
            if self.running_down:
                pyautogui.scroll(-10)
            if not (self.running_up or self.running_down):  
                break

    def start_scroll_up(self):
        if not self.running_up:  
            self.running_up = True
            if not self.is_alive():  
                self.start()
            if self.running_down:  
                self.running_down = False

    def start_scroll_down(self):
        if not self.running_down:  
            self.running_down = True
            if not self.is_alive():  
                self.start()
            if self.running_up: 
                self.running_up = False

    def stop_scroll_up(self):
        self.running_up = False

    def stop_scroll_down(self):
        self.running_down = False

    def stop_scroll(self):
        self.running_up = False
        self.running_down = False
