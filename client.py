import time

import win32api
import win32con
import win32gui
import win32process
import random

import win32gui
import pyautogui
from detection.image_rec import (
    find_references,
    get_first_location,
    make_reference_image_list,
)

from image_to_text import read_image_text

# def show_image(image):
#     import numpy
#     from matplotlib import pyplot as plt

#     iar = numpy.array(image)
#     plt.imshow(iar)
#     plt.show()


def scroll_down():
    pyautogui.press("pagedown")


def orientate_chrome(logger):
    window_name = (
        "Discover the top streamed music and songs online on Soundcloud - Google Chrome"
    )
    width = 1200
    height = 1200
    x = 5
    y = 5

    # Get the window handle based on the window name
    hwnd = win32gui.FindWindow(None, window_name)

    if hwnd == 0:
        logger.log(f"Window '{window_name}' not found.")
        return

    # Get the current window position and size
    _, _, wnd_width, wnd_height = win32gui.GetClientRect(hwnd)
    wnd_x, wnd_y, _, _ = win32gui.GetWindowRect(hwnd)

    # Calculate the new window position and size
    new_width = width if width is not None else wnd_width
    new_height = height if height is not None else wnd_height
    new_x = x if x is not None else wnd_x
    new_y = y if y is not None else wnd_y

    # Resize and move the window
    win32gui.MoveWindow(hwnd, new_x, new_y, new_width, new_height, True)


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


def list_window_names(logger):
    def enum_window_callback(hwnd, window_names):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            if window_title:
                window_names.append(window_title)

    window_names = []
    win32gui.EnumWindows(enum_window_callback, window_names)

    for n in window_names:
        logger.log(n)


def screenshot(region=(0, 0, 1400, 1400)):
    if region is None:
        return pyautogui.screenshot()  # type: ignore
    return pyautogui.screenshot(region=region)  # type: ignore
