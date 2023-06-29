import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from UTILS.chrome_interaction import (
    check_for_nothing_to_hear_here_on_profile_page,
    check_for_old_upload_text,
    read_follower_count_of_this_profile,
)

from UTILS.file_handler import add_to_good_links
from UTILS.chrome_driver import make_chrome_driver
from UTILS.file_handler import remove_and_return_random_raw_link
from UTILS.chrome_interaction import wait_for_this_profile_page_to_load


FOLLOWER_UPPER_LIMIT = 400
FOLLOWER_LOWER_LIMIT = 15


def check_one_unchecked_link_2(driver):
    # open to 1 link from the file
    link = remove_and_return_random_raw_link()
    try:
        driver.get(link)
    except:
        print(f"Failure getting to {link}")
        return "url fail"

    # Wait for the webpage to load
    webpage_wait_start_time = time.time()
    wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(4)
    print(
        f"Waited {str(time.time() - webpage_wait_start_time)[:4]} seconds for webpage"
    )

    profile_check_return = check_this_profile(driver)

    if profile_check_return != "good":
        return profile_check_return
    else:
        # write the link to the good links file
        append_method_return = add_to_good_links(link)
        if append_method_return == "Error writing to file":
            return "Write fail"

    return "success"


def check_one_unchecked_link_2_wrapper(driver):
    start_time = time.time()

    out = check_one_unchecked_link_2(driver)

    time_taken = str(time.time() - start_time)[:4]

    if out == "success":
        print(f"Good profile! {time_taken}")
    elif out == "Write fail":
        print(f"Failed to write this profile url to the good links file {time_taken}")
    elif out == "url fail":
        print(f"Failed to get to this url {time_taken}")
    else:
        print(f"Bad profile for reason [{out}] {time_taken}")


def check_one_unchecked_link():
    driver = make_chrome_driver()

    # open to 1 link from the file
    link = remove_and_return_random_raw_link()
    try:
        driver.get(link)
    except:
        print(f"Failure getting to {link}")
        return

    # Wait for the webpage to load
    wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(4)

    profile_check_return = check_this_profile(driver)

    if profile_check_return != "good":
        return profile_check_return
    else:
        # write the link to the good links file
        append_method_return = add_to_good_links(link)
        if append_method_return == "Error writing to file":
            return "Write fail"

    return "success"


def check_this_profile(driver):
    wait_for_this_profile_page_to_load(driver)

    # if 'nothing to hear here' is on the page, return
    if check_for_nothing_to_hear_here_on_profile_page(driver):
        return "No recent uploads"

    # if most recent repub/post is older than 6mo, return 'fail
    old_upload_text_return = check_for_old_upload_text(driver)
    if old_upload_text_return:
        return f"No recent uploads {old_upload_text_return}"

    # read this follower count
    count = read_follower_count_of_this_profile(driver)

    if count == "fail":
        return "Follower count read fail"
    count = parse_follower_count(count)
    count = int(count)

    # if follower count is too high return
    if count > FOLLOWER_UPPER_LIMIT:
        return "Follower count too high"

    # if follower count is too low return
    if count < FOLLOWER_LOWER_LIMIT:
        return "Follower count too low"

    return "good"


def parse_follower_count(count):
    count = count.replace(",", "")
    if "K" in count or "k" in count:
        count = count.replace("K", "")
        count = float(count) * 1000

    elif "M" in count or "m" in count:
        count = count.replace("M", "")
        count = float(count) * 1000000

    return count


def check_one_unchecked_link_wrapper():
    start_time = time.time()
    out = check_one_unchecked_link()
    time_taken = str(time.time() - start_time)[:5]

    if out == "success":
        print(f"Success in {time_taken} seconds")

    else:
        print(f"Failure in {time_taken} seconds for reason: {out}")


if __name__ == "__main__":
    pass
