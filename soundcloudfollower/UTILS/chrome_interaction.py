import time

from selenium.webdriver.common.by import By


def check_for_nothing_to_hear_here_on_profile_page(driver):
    try:
        path = "/html/body/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[2]/div/div/h3"
        element = driver.find_element(By.XPATH, path)
        text = element.text
        if "Nothing to hear here" in text:
            return True
    except:
        return False


def scroll_to_bottom(driver):
    """method to scroll to the bottom of the page as far as it has loaded

    Args:
        driver (selenium.webdriver.chrome.webdriver.WebDriver): the selenium chrome driver
        logger (logging.Logger): the logger

    Returns:
        None

    """
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def find_names(driver):
    name_list = []

    for index in range(500):
        try:
            path = f"/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/ul/li[{index}]/div/div[2]/a"
            element = driver.find_element(By.XPATH, path)
            name_list.append(element.text)
        except:
            pass

    return parse_name_list(name_list)


def parse_name_list(strings):
    blacklist = [
        "🏽",
        "🥷",
        "🔥",
        "₉",
        "⁹",
        "☢️",
        "₉",
        "⁹",
        "₉",
        "💯",
        "⚡",
        "🧛🏾🏾",
        "🧛",
        "💕",
        "😦",
        "蚊",
        "💔",
        "ự",
        "ỡ",
        "ن",
        "✨",
        "ё",
        ".",
        "_",
        "й",
        "$",
        "<",
        "ℳ",
        "ℛ",
        "ا",
        "هي",
        "🥴",
        "يم",
        "з",
        "Л",
        "ê",
        "ô",
        "&",
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "-",
        "=",
        "Ž",
        "é",
        "[",
        "]",
    ]

    good_strings = []
    for this_string in strings:
        has_blacklist = False
        for this_blacklist in blacklist:
            if this_blacklist in this_string:
                has_blacklist = True
                break
        if not has_blacklist:
            good_strings.append(this_string)
    return good_strings


def read_following_count_of_this_profile(driver):
    TIMEOUT = 5

    start_time = time.time()
    while 1:
        time_taken = time.time() - start_time
        if time_taken > TIMEOUT:
            return "fail"

        try:
            path = "/html/body/div[1]/div[2]/div[2]/div/div[4]/div[2]/div/article[1]/table/tbody/tr/td[2]/a/div"
            element = driver.find_element(By.XPATH, path)
            return element.text
        except:
            pass


def read_follower_count_of_this_profile(driver):
    TIMEOUT = 5

    start_time = time.time()
    while 1:
        time_taken = time.time() - start_time
        if time_taken > TIMEOUT:
            return "fail"

        try:
            path = "/html/body/div[1]/div[2]/div[2]/div/div[4]/div[2]/div/article[1]/table/tbody/tr/td[1]/a/div"
            element = driver.find_element(By.XPATH, path)
            return element.text
        except:
            pass


def wait_for_this_profile_page_to_load(driver):
    start_time = time.time()

    while not check_for_old_upload_text(driver):
        time_taken = time.time() - start_time
        if time_taken > 10:
            return "fail"

    time.sleep(1)
    print(f"Waited {str(time.time() - start_time)[:5]}s for this profile page")


def check_for_old_upload_text(driver):
    path = "/html/body/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[2]/div/div[2]/ul/li[1]/div/div/div/div[2]/div[1]/div/div/div[3]/div[1]/time/span[2]"
    try:
        element = driver.find_element(By.XPATH, path)
        text = element.text
        if "year ago" in text or "years ago" in text:
            return text
        if (
            "6 months ago" in text
            or "7 months ago" in text
            or "8 months ago" in text
            or "9 months ago" in text
            or "10 months ago" in text
            or "11 months ago" in text
        ):
            return text

    except:
        return False
