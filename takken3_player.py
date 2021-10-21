import pyautogui
import time

if __name__ == '__main__':
    for i in range(4):
        time.sleep(1)
        pyautogui.keyDown('z')
        # pyautogui.hotkey('down', 's', 'a')
        # pyautogui.press('down')
        # time.sleep(1)
        # pyautogui.press('down')
        # pyautogui.hotkey('down', 's', 'a')