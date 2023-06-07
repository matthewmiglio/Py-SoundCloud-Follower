import time

from selenium.webdriver.common.by import By


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

    # print(f'Found {len(name_list)} raw names')

    return parse_name_list(name_list)


def parse_name_list(strings):
    blacklist = [
        "🏽",
        "🥷" ,
        "🔥",
        '₉',
        '⁹',
        '☢️',
        '₉',
        '⁹',
        '₉',
        '💯',
        '⚡',
        '🧛🏾🏾',
        '🧛',
        '💕',
        '😦',
        '蚊',
        '💔',
        'ự',
        'ỡ',
        'ن',
        '✨',
        'ё',
        '.',
        '_',
        'й',
        '$',
        '<',
        'ℳ',
        'ℛ',
        'ا',
        'هي',
        '🥴',
        'يم',
        'з',
        'Л',
        'ê',
        'ô',
        '&',
        '!',
        '@',
        '#',
        '$',
        '%',
        '^',
        '&',
        '*',
        '(',
        ')',
        '-',
        '=',
        'Ž',
        'é',
        '[',
        ']',
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


def read_follower_count_of_this_profile(driver):
    READ_FOLLOWER_COUNT_TIMEOUT = 5

    start_time = time.time()
    while 1:
        time_taken = time.time() - start_time
        if time_taken>READ_FOLLOWER_COUNT_TIMEOUT:return 'fail'

        try:
            path = '/html/body/div[1]/div[2]/div[2]/div/div[4]/div[2]/div/article[1]/table/tbody/tr/td[1]/a/div'
            element = driver.find_element(By.XPATH, path)
            return element.text
        except:
            pass