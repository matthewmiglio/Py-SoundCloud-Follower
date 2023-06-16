import win32gui

import subprocess


def launch_soundcloud():
    # close_chrome_windows()
    open_soundcloud_in_chrome()


def close_chrome_windows():
    subprocess.Popen("taskkill /im chrome.exe /f", shell=True)


def open_soundcloud_in_chrome():
    # Start Chrome and open the URL
    subprocess.Popen(
        [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            "https://soundcloud.com",
        ],
        close_fds=True,
    )


def open_chrome_webpage(url):
    # Start Chrome and open the URL
    subprocess.Popen(
        [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            url,
        ],
        close_fds=True,
    )


def orientate_chrome():
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
        print(f"Window '{window_name}' not found.")
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
