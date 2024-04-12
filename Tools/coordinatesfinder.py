import pyautogui

try:
    while True:
        # Get and print the current mouse coordinates
        x, y = pyautogui.position()
        print(f"X: {x}, Y: {y}", end='\r')
except KeyboardInterrupt:
    print("\nProgram terminated.")
    