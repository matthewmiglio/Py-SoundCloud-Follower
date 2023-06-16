import time
import random
from RAW_SOUNDCLOUD_URL_FINDER.raw_link_finder import soundcloud_url_finder_main_loop
from RAW_URL_CHECKER.url_checker import check_one_unchecked_link
from USER_DATA_READER.read_user_data import record_user_data
from UTILS.chrome_driver import make_chrome_driver
from UTILS.file_handler import (
    get_good_links_count,
    get_raw_links_count,
)


def url_finder_state_tree(driver, state,soundcloud_raw_links_upper_limit):
    if state == "get_soundcloud_urls":
        state = get_soundcloud_urls_state(driver,soundcloud_raw_links_upper_limit,)

    elif state == "get_good_links":
        state = check_raw_links_state(driver)

    return state


def get_soundcloud_urls_state(driver, soundcloud_raw_links_upper_limit):
    # get links of profiles until the file has soundcloud_raw_links_upper_limit lines
    line_count = get_raw_links_count()
    while line_count < soundcloud_raw_links_upper_limit:
        start_time = time.time()

        writes = soundcloud_url_finder_main_loop(driver)
        line_count = get_raw_links_count()

        print(
            f"Wrote {writes} urls to list of {line_count} urls in {str(time.time() - start_time)[:5]} seconds"
        )

    return "get_good_links"


def check_raw_links_state(driver):
    # while line count of raw links is above 5
    line_count = get_raw_links_count()
    while line_count > 5:
        # record_user_data() sometimes
        if random.randint(0, 10) == 1:
            record_user_data()

        loop_start_time = time.time()

        check_return = check_one_unchecked_link(driver=driver)

        if check_return != "success":
            print(
                f"Failed  in {str(time.time() - loop_start_time)[:5]} seconds. [{get_good_links_count()} good accounts] Reason: ({check_return})"
            )
        else:
            print(
                f"Success in {str(time.time() - loop_start_time)[:5]} seconds. [{get_good_links_count()} good accounts] "
            )

        # line count = get_soundcloud_links_line_count()
        line_count = get_raw_links_count()
    return "get_soundcloud_urls"


def url_finding_main(soundcloud_raw_links_upper_limit):
    # figure out which state to run: if there are less than 1000 links, get more links, else check the links
    line_count = get_raw_links_count()
    print(f"There are {line_count} unverified links remaining in the file system")
    if line_count < soundcloud_raw_links_upper_limit / 2:
        state = "get_soundcloud_urls"
    else:
        state = "get_good_links"

    # make driver, start loop
    driver = make_chrome_driver()
    while 1:
        state = url_finder_state_tree(driver, state,soundcloud_raw_links_upper_limit)
