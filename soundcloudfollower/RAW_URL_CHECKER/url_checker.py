from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from UTILS.chrome_interaction import check_for_nothing_to_hear_here_on_profile_page, check_for_old_upload_text, read_follower_count_of_this_profile

from UTILS.file_handler import add_to_good_links, remove_and_return_random_raw_link


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


def check_one_unchecked_link(driver):
    # get 1 link from the file
    link = remove_and_return_random_raw_link()

    # open to that link
    driver.get(link)

    # Wait for the webpage to load
    wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(2)

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

    # write the link to the good links file
    append_method_return = add_to_good_links(link)
    if append_method_return == "Error writing to file":
        return "Write fail"

    return "success"


# driver = make_chrome_driver()
# driver.get("https://soundcloud.com/Connor-p")

# while 1:
#     print(check_for_old_upload_text(driver))
#     pass


# https://soundcloud.com/Connor-p (uploaded 3 years ago), failed to read that
# https://soundcloud.com/Kavon-Edwards (uploaded 6 years ago), failed to read that
