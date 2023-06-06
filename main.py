import time
import random
from client import orientate_chrome, scroll_down
from follow_randoms import (
    follow_1_person_from_follower_list_page,
)
from launcher import launch_soundcloud
from logger import Logger
from navigation import (
    get_to_follower_list_of_this_profile,
    get_to_rapper_page,
)


accounts_to_examine = [
    "jahseh-onfroy",
    "kanyewest",
    "pharrellwilliams-official",
    "cudderland",
    "kendrick-lamar-music",
    "joeybadass",
    "asvpxrocky",
    "tylerthecreatorofficial",
    "denzelcurryph",
    "jackharlow",
    "cordae",
    "chancetherapper",
    "hykeemcarter",
    "logic_official",
    "vince-staples-official",
    "larryfisherman",
    "dj-khaled",
    "pouya-kevin",
    "offset-sc",
    "migosatl",
    "scrim",
    "meek-mill-dc",
    "torylanez",
    "harlem_fetty",
    "a-boogie-wit-da-hoodie",
    "rich-the-kid",
    "futureisnow",
    "quavoofficial",
    "youngthugworld",
    "youngma",
    "destroylonely",
    "moneybagg-yo",
    "estgee",
    "megan-thee-stallion",
    "jayelectronica",
    "roddyricch",
    "dabilliondollarbaby",
    "fivioforeign",
    "gherbo",
    "bennythebutcher1",
    "boldyjames",
    "lupefiasco",
    "jay-z-official",
    "earlxsweatshirtmusic",
    "germone",
    "lildurk",
    "nba-youngboy",
    "eslabonarmado",
    "toosii2x",
    "lilmabu",
    "djschemee",
    "770rd",
    "lil-baby-4pf",
    "yungcochise",
    "evolvefrmpain",
    "octobersveryown",
    "ingblakedagr8",
    "travis-scott-radio",
    "lil-kizzle",
    "lilyeat",
    "21savage",
    "rodwave",
    "boob7",
    "lileazzyy",
    "imrealugly",
    "trap-land-rd",
    "dkanimebit",
    "nlechoppa",
    "metroboomin",
    "tee-grizzley",
    "jordan-medinger",
    "luhtylermusic",
    "heisrema",
    "zafemmusic",
]
TARGET_FOLLOW_COUNT = 10
RAPPER_SEGMENTS = 5
WAIT_TIME = 576


# method to print any dupe strings in a string list
def check_for_dupe_accounts():
    dupe_strings = []
    for account_string in accounts_to_examine:
        if account_string in dupe_strings:
            print(account_string)
        else:
            dupe_strings.append(account_string)


def main_loop(logger):
    logger.log("First log")

    # calculate follows per rapper
    follows_per_rapper = TARGET_FOLLOW_COUNT / RAPPER_SEGMENTS

    # select random rappers for each segment
    rappers = []
    for _ in range(RAPPER_SEGMENTS):
        rappers.append(random.choice(accounts_to_examine))

    for rapper in rappers:
        logger.log(f"{rapper: <20}: {follows_per_rapper} follows...")

    # for each rapper in the list
    for rapper in rappers:
        logger.log(f"Beginning following loop for {rapper}")
        logger.add_rapper_used()

        # orientate chrome
        orientate_chrome(logger)

        # get to rapper page
        logger.log(f"Getting to {rapper}'s page")
        if get_to_rapper_page(logger, rapper) == "restart":
            return "restart"

        # click followers button
        logger.log(f"Getting to {rapper}'s followers list page")
        if get_to_follower_list_of_this_profile(logger) == "restart":
            return "restart"

        # follow users until limit reached for this segment
        logger.log(f"Starting follow loop for {rapper}")
        follow_count = 0
        while follow_count < follows_per_rapper:
            start_time = time.time()

            # follow 1 random
            logger.log("Following 1 person from this list")
            if follow_1_person_from_follower_list_page(logger) == "restart":
                return "restart"
            logger.add_follow()

            # incremenet count
            follow_count += 1

            # wait until its been WAIT_TIME since start_time
            wait_start_time = time.time()
            prints = 0
            time_to_wait = WAIT_TIME - (time.time() - start_time)
            while time_to_wait > 0:
                time_to_wait = WAIT_TIME - (time.time() - start_time)
                time_waiting = time.time() - wait_start_time
                if time_waiting >= prints * 10:
                    logger.log(f"Waiting {str(time_to_wait)[:5]} seconds...")
                    prints += 1

            # scroll down random amount
            logger.log("Scrolling down in followers list")
            for _ in range(random.randint(4, 8)):
                scroll_down()


def main():
    # make logger object
    logger = Logger()

    # launch soundcloud on chrome
    launch_soundcloud()

    while 1:
        if main_loop(logger) == "restart":
            logger.log("Restarting...")

            # close chrome
            # close_chrome_windows()

            # launch soundcloud on chrome
            launch_soundcloud()

            # incremenet logger
            logger.add_restart()


main()
# check_for_dupe_accounts(accounts_to_examine)
# print(len(accounts_to_examine))
