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
    pyautogui.press('pagedown')

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


def send_keys(logger,window_name, text, x_coord=None, y_coord=None):
    # Get the handle of the currently active window
    active_window = win32gui.GetForegroundWindow()

    # Find the window based on the window name
    hwnd = win32gui.FindWindow(None, window_name)
    if hwnd == 0:
        logger.log("Window not found.")
        return

    # Get the window's process ID and thread ID
    _, process_id = win32process.GetWindowThreadProcessId(hwnd)

    # Open the process with required permissions
    process_handle = win32api.OpenProcess(
        win32con.PROCESS_ALL_ACCESS, False, process_id
    )

    # Set the window as the foreground window
    win32gui.SetForegroundWindow(hwnd)

    # Click the spot to type into if x and y coordinates are provided
    if x_coord is not None and y_coord is not None:
        # Click action
        click_x = x_coord
        click_y = y_coord
        win32api.SetCursorPos((click_x, click_y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, click_x, click_y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, click_x, click_y, 0, 0)
        time.sleep(0.1)

    # Send each keystroke to the window
    for character in text:
        virtual_key = win32api.VkKeyScan(character)
        scan_code = win32api.MapVirtualKey(virtual_key, 0)
        win32api.keybd_event(virtual_key, scan_code, win32con.KEYEVENTF_EXTENDEDKEY, 0)
        win32api.keybd_event(
            virtual_key,
            scan_code,
            win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP,
            0,
        )

    # Delay to allow the target window to process the input
    time.sleep(0.1)

    # Restore focus to the previously active window
    win32gui.SetForegroundWindow(active_window)

    # Close the process handle
    win32api.CloseHandle(process_handle)


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
