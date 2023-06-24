import time
import numpy

from UTILS.chrome_launcher import (
    close_chrome_windows,
    open_chrome_webpage,
    orientate_chrome,
)
from UTILS.clicking import click
from UTILS.file_handler import return_and_delete_last_line_in_good_urls
from UTILS.image_rec import pixel_is_equal, screenshot
import random

from USER_DATA_READER.read_user_data import record_user_data


def follow_main(follow_count):
    # open chrome
    open_chrome_webpage(url="https://soundcloud.com/discover")
    time.sleep(3)
    orientate_chrome()

    # track follows as we loop
    follows = 0

    # record user data before starting follow loop
    record_user_data()

    CHROME_TAB_RESTART_COUNT_RANGE = (10, 16)

    chrome_tab_limit = random.randint(
        CHROME_TAB_RESTART_COUNT_RANGE[0], CHROME_TAB_RESTART_COUNT_RANGE[1]
    )

    while 1:
        # track loop time
        start_time = time.time()

        # if reached amount of people to follow, break from follow loop
        if follows == follow_count:
            break

        # every 7 users, restart chrome
        if follows % chrome_tab_limit == 0 and follows != 0:
            # restart chrome
            close_chrome_windows()
            open_chrome_webpage(url="https://soundcloud.com/discover")
            time.sleep(3)
            orientate_chrome()

        # get a link
        this_good_url = return_and_delete_last_line_in_good_urls()

        # get to link
        open_chrome_webpage(url=this_good_url)
        time.sleep(3)

        # if already following, break
        if check_if_following_user():
            print(
                f"Failure    following #{follows} in {str(time.time() - start_time)[:5]} seconds"
            )
            continue

        # follow
        click_follow_on_this_profile_page()
        follows += 1

        print(
            f"Successful following #{follows} in {str(time.time() - start_time)[:5]} seconds"
        )

    # record user data after finishing follow loop
    record_user_data()


def click_follow_on_this_profile_page():
    follow_button_coord = [909, 417]
    click(follow_button_coord[0], follow_button_coord[1])


def check_if_following_user():
    iar = numpy.asarray(screenshot())
    pixel = iar[424][877]
    if pixel_is_equal([255, 255, 255], pixel, tol=25):
        return True
    return False


if __name__ == "__main__":
    # get a link
    this_good_url = return_and_delete_last_line_in_good_urls()

    # get to link
    open_chrome_webpage(url=this_good_url)
    time.sleep(3)