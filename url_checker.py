from chrome_interaction import (
    check_for_nothing_to_hear_here_on_profile_page,
    check_for_old_upload_text,
    read_follower_count_of_this_profile,
)
from file_handler import add_to_good_links, remove_and_return_oldest_links_line
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


FOLLOWER_UPPER_LIMIT = 400
FOLLOWER_LOWER_LIMIT = 15


def parse_follower_count(count):
    count = count.replace(",", "")
    if "K" in count or "k" in count:
        count = count.replace("K", "")
        count = float(count) * 1000

    elif "M" in count or "m" in count:
        count = count.replace("M", "")
        count = float(count) * 1000000

    return count


def soundcloud_url_checker_main_loop(driver):
    # get 1 link from the file
    link = remove_and_return_oldest_links_line()

    # open to that link
    driver.get(link)

    # Wait for the webpage to load
    wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # if 'nothing to hear here' is on the page, return
    if check_for_nothing_to_hear_here_on_profile_page(driver):
        return "fail"

    # if most recent repub/post is older than 6mo, return 'fail
    if check_for_old_upload_text(driver) == True:
        return "fail"

    # read this follower count
    count = read_follower_count_of_this_profile(driver)

    if count == "fail":
        return "fail"
    count = parse_follower_count(count)
    count = int(count)

    # if follower count is too high return
    if count > FOLLOWER_UPPER_LIMIT:
        return "fail"

    # if follower count is too high return
    if count < FOLLOWER_LOWER_LIMIT:
        return "fail"

    # write the link to the good links file
    append_method_return = add_to_good_links(link)
    if append_method_return == "Error writing to file":
        return "fail"

    return "success"
