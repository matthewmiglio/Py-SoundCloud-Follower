import numpy
from client import click, screenshot, scroll_down
from detection.image_rec import pixel_is_equal
from image_to_text import read_image_text
import random
import time
from navigation import (
    check_if_on_a_profile,
    check_if_on_followers_list_page,
    wait_for_follower_list_page,
)


def follow_1_person_from_follower_list_page(logger):
    logger.log("Following 1 person from follower list page")
    while 1:
        # get to a random profile on this rapper's follower list
        if get_to_random_profile_on_this_followers_list_page(logger)=='restart':return 'restart'

        # read follow count
        follow_count_of_this_profile = get_follower_count_of_this_profile()

        # if fail read, return to follower list, try again
        if follow_count_of_this_profile == "Fail read":
            logger.log("Failed to read follow count, trying again")
            return_to_follower_list_from_random_profile()
            continue

        # cast to int
        follow_count_of_this_profile = int(follow_count_of_this_profile)

        logger.log(f"This profile's follower count is {follow_count_of_this_profile}")

        # if follow count exceeds limits, return to follower list, try again
        FOLLOW_COUNT_UPPER_LIMIT = 200
        FOLLOW_COUNT_LOWER_LIMIT = 5
        if (follow_count_of_this_profile > FOLLOW_COUNT_UPPER_LIMIT) or (
            follow_count_of_this_profile < FOLLOW_COUNT_LOWER_LIMIT
        ):
            logger.log("This profile has too many followers, trying again")
            if return_to_follower_list_from_random_profile(logger) == "restart":
                return "restart"
            continue

        # if already following this user, return to follower list, try again
        if check_if_following_user():
            logger.log("Already following this user, trying again")
            if return_to_follower_list_from_random_profile(logger) == "restart":
                return "restart"
            continue

        # follow this user
        follow_button_coords = [900, 502]
        click(follow_button_coords[0], follow_button_coords[1])
        if return_to_follower_list_from_random_profile(logger) == "restart":
            return "restart"
        break


def check_if_following_user():
    iar = numpy.asarray(screenshot())
    pixel = iar[502][900]
    if pixel_is_equal([255, 255, 255], pixel, tol=25):
        return True
    return False


def return_to_follower_list_from_random_profile(logger):
    browser_back_button_coord = [32, 65]
    click(browser_back_button_coord[0], browser_back_button_coord[1])
    if wait_for_follower_list_page(logger) == "restart":
        return "restart"


def get_follower_count_of_this_profile():
    text = read_image_text(
        image=screenshot(region=[800, 574, 134, 43]),
        segmentation_mode="single_line",
        engine_mode="default",
    )

    try:
        if "M" in text:
            text = text.replace("M", "")
            text = float(text)
            text *= 1000000
            text = int(text)

        elif "K" in text:
            text = text.replace("K", "")
            text = float(text)
            text *= 1000
            text = int(text)

        elif "," in text:
            text = text.replace(",", "")
            text = int(text)

        return text
    except:
        return "Fail read"


def get_to_random_profile_on_this_followers_list_page(logger):
    if random.randint(0, 3) == 1:
        logger.log(
            "Random scroll for get_to_random_profile_on_this_followers_list_page()"
        )
        time.sleep(3)
        scroll_down()

    logger.log("getting to a random profile on this follower list page")

    while check_if_on_followers_list_page():
        click_random_profile_on_followers_page()
        time.sleep(1)

    if not check_if_on_a_profile():
        return 'restart'


def click_random_profile_on_followers_page():
    coord_list = [
        [48, 618],
        [249, 618],
        [442, 615],
        [639, 611],
        [832, 626],
        [1029, 622],
        [44, 796],
        [241, 789],
        [438, 789],
        [635, 793],
        [825, 778],
        [1029, 778],
        [40, 1058],
        [245, 1065],
        [438, 1062],
        [631, 1065],
        [828, 1062],
        [1021, 1062],
    ]

    random_coord = random.choice(coord_list)
    click(random_coord[0], random_coord[1])
