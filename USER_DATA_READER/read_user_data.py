import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UTILS.chrome_driver import make_chrome_driver
from UTILS.chrome_interaction import (
    read_follower_count_of_this_profile,
    read_following_count_of_this_profile,
)
from UTILS.file_handler import append_to_user_data_file


def record_user_data():
    # make a driver
    driver = make_chrome_driver()

    print("Recording user data")

    # get to mattproduction's profile
    url = "https://soundcloud.com/mattproduction"
    driver.get(url)

    # Wait for the webpage to load
    wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    time.sleep(2)

    # read following vs follower values
    follower_value = read_follower_count_of_this_profile(driver)
    following_value = read_following_count_of_this_profile(driver)

    # make data line
    data_line = f"{get_current_time()}///{follower_value}///{following_value}"

    # write data line to file
    append_to_user_data_file(data_line)

    print("Done recording data...")
    print(f'Recorded this line: "{data_line}"')


def get_current_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    return current_time
