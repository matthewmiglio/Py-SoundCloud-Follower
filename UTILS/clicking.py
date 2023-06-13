import pyautogui
import time


def click(x, y, clicks=1, interval=0.0, duration=0.1, button="left"):
    # get current moust position
    origin = pyautogui.position()

    # move the mouse to the spot
    pyautogui.moveTo(x, y, duration=duration)

    # click it as many times as ur suppsoed to
    loops = 0
    while loops < clicks:
        pyautogui.click(x=x, y=y, button=button)
        loops += 1
        time.sleep(interval)

    # move mouse back to original position
    pyautogui.moveTo(origin[0], origin[1])
