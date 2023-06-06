import numpy

from client import click, screenshot
import pyautogui
import time

from detection.image_rec import pixel_is_equal

url_search_bar_coords = [193, 67]

rapper_page_followers_button_coords = [844, 577]


def wait_for_follower_list_page(logger):
    start_time = time.time()
    while 1:
        if time.time() - start_time > 10:
            logger.log("Waited 10s for follower list page, but it never came")
            return "restart"

        if check_if_on_followers_list_page():
            break


def check_if_on_followers_list_page():
    iar = numpy.asarray(screenshot())

    black_followers_of_text_exists = False
    for x in range(180, 280):
        this_pixel = iar[205][x]
        if pixel_is_equal([51, 51, 51], this_pixel, tol=25):
            black_followers_of_text_exists = True
            break

    orange_followers_text_exists = False
    for x in range(250, 290):
        this_pixel = iar[339][x]
        if pixel_is_equal([255, 85, 0], this_pixel, tol=25):
            orange_followers_text_exists = True
            break

    white_background_exists = True
    for x in range(500, 900):
        for y in range(325, 350):
            this_pixel = iar[y][x]
            if not (pixel_is_equal([255, 255, 255], this_pixel, tol=25)):
                white_background_exists = False
                break

    if (
        black_followers_of_text_exists
        and orange_followers_text_exists
        and white_background_exists
    ):
        return True
    return False


def get_to_rapper_page(logger,random_account_to_examine):
    # should start on 'Discover the top streamed music and songs online on Soundcloud - Google Chrome'
    logger.log("getting to rapper page")

    # click url search bar
    logger.log("Clicking search box")
    click(
        x=url_search_bar_coords[0],
        y=url_search_bar_coords[1],
    )

    # make url
    url = f"https://soundcloud.com/{random_account_to_examine}"

    # type url
    logger.log(f"Typing url {url}")
    pyautogui.typewrite(url)

    # press enter
    pyautogui.press("enter")

    # wait for page to load
    ("Waiting 4s for page load")
    if wait_for_a_profile_page(logger)=='restart':return 'restart'

    logger.log("Made it to rapper page")


def get_to_follower_list_of_this_profile(logger):
    logger.log("Getting to follower list")

    logger.log("Clicking the rapper's follower list button")

    click(
        x=rapper_page_followers_button_coords[0],
        y=rapper_page_followers_button_coords[1],
    )
    if wait_for_follower_list_page(logger)=='restart':return 'restart'


def wait_for_a_profile_page(logger):
    start_time = time.time()
    while not check_if_on_a_profile():
        time_taken = time.time() - start_time
        if time_taken > 10:
            logger.log("#6314456 Failure with wait_for_a_profile_page()")
            return "restart"


def check_if_on_a_profile():
    iar = numpy.asarray(screenshot())

    orange_all_text_exists = False
    for x in range(35, 70):
        this_pixel = iar[506][x]
        if pixel_is_equal([255, 85, 0], this_pixel, tol=25):
            orange_all_text_exists = True
            break

    black_popular_tracks_text_exists = False
    for x in range(90, 135):
        this_pixel = iar[506][x]
        if pixel_is_equal([51, 51, 51], this_pixel, tol=25):
            black_popular_tracks_text_exists = True
            break

    grey_followers_text_exists = False
    for x in range(810, 860):
        this_pixel = iar[593][x]
        if pixel_is_equal([153, 153, 153], this_pixel, tol=25):
            grey_followers_text_exists = True
            break

    if (
        orange_all_text_exists
        and black_popular_tracks_text_exists
        and grey_followers_text_exists
    ):
        return True
    return False
