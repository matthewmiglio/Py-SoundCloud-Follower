import subprocess
import time


def launch_soundcloud():
    # close_chrome_windows()
    open_soundcloud_in_chrome()
    time.sleep(5)


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


# close_chrome_windows()
