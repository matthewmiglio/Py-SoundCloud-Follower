from chrome_interaction import read_follower_count_of_this_profile
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
    # print("---------------------------------------")
    loop_start_time = time.time()

    # get 1 link from the file
    link = remove_and_return_oldest_links_line()

    # open to that link
    webpage_loading_start_time = time.time()
    driver.get(link)

    # Wait for the webpage to load
    wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    # print(
    #     f"Took {str(time.time()  - webpage_loading_start_time)[:5]} seconds to load the webpage"
    # )

    # read this follower count
    count = read_follower_count_of_this_profile(driver)

    if count == "fail":
        # print(f"Looped in {str(time.time() - loop_start_time)[:5]} seconds")
        return "fail"
    count = parse_follower_count(count)
    count = int(count)

    # print(f"This follower count is: {count}")

    # if follower count is too high return
    if count > FOLLOWER_UPPER_LIMIT:
        # print(f"Count of {count} is too high")
        # print(f"Looped in {str(time.time() - loop_start_time)[:5]} seconds")
        return "fail"

    # if follower count is too high return
    if count < FOLLOWER_LOWER_LIMIT:
        # print(f"Count of {count} is too low")
        # print(f"Looped in {str(time.time() - loop_start_time)[:5]} seconds")
        return "fail"

    # write the link to the good links file
    append_method_return = add_to_good_links(link)
    if append_method_return == "Error writing to file":
        # print(f"Looped in {str(time.time() - loop_start_time)[:5]} seconds")

        return "fail"

    # print(f"Looped in {str(time.time() - loop_start_time)[:5]} seconds")
    return "success"
