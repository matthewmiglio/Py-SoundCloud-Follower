import time
from chrome_driver import make_chrome_driver
from file_handler import get_good_links_line_count, get_soundcloud_links_line_count
from url_checker import soundcloud_url_checker_main_loop
from raw_link_finder import soundcloud_url_finder_main_loop

SOUNDCLOUD_LINKS_UPPER_LIMIT = 1000


def state_tree(driver, state):
    if state == "get_soundcloud_urls":
        state = get_soundcloud_urls_state(driver)

    elif state == "get_good_links":
        state = get_good_links_state(driver)

    return state


def get_soundcloud_urls_state(driver):
    # get links of profiles until the file has SOUNDCLOUD_LINKS_UPPER_LIMIT lines
    line_count = get_soundcloud_links_line_count()
    while line_count < SOUNDCLOUD_LINKS_UPPER_LIMIT:
        start_time = time.time()

        writes = soundcloud_url_finder_main_loop(driver)
        line_count = get_soundcloud_links_line_count()

        print(
            f"Wrote {writes} urls to list of {line_count} urls in {str(time.time() - start_time)[:5]} seconds"
        )

    return "get_good_links"


def get_good_links_state(driver):
    # while line count of raw links is above 5
    line_count = get_soundcloud_links_line_count()
    while line_count > 5:
        loop_start_time = time.time()

        if soundcloud_url_checker_main_loop(driver=driver) == "fail":
            print(
                f"Failed  in {str(time.time() - loop_start_time)[:5]} seconds. [{get_good_links_line_count()} good accounts...] "
            )
        else:
            print(
                f"Success in {str(time.time() - loop_start_time)[:5]} seconds. [{get_good_links_line_count()} good accounts...] "
            )

        # line count = get_soundcloud_links_line_count()
        line_count = get_soundcloud_links_line_count()
    return "get_soundcloud_urls"


def url_finding_main():
    # figure out which state to run: if there are less than 1000 links, get more links, else check the links
    line_count = get_soundcloud_links_line_count()
    print(f"There are {line_count} unverified links remaining in the file system")
    if line_count < SOUNDCLOUD_LINKS_UPPER_LIMIT / 2:
        state = "get_soundcloud_urls"
    else:
        state = "get_good_links"

    # make driver, start loop
    driver = make_chrome_driver()
    while 1:
        state = state_tree(driver, state)


