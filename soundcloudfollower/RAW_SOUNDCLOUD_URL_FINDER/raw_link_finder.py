from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from UTILS.chrome_interaction import find_names, scroll_to_bottom

from UTILS.file_handler import append_to_raw_links_file
from UTILS.chrome_driver import make_chrome_driver


LIKES_LINKS = [
    "https://soundcloud.com/lildurk/war-bout-it/likes",
    "https://soundcloud.com/destroylonely/how-you-feel-main/likes",
    "https://soundcloud.com/jahseh-onfroy/hearteater/likes",
    "https://soundcloud.com/rojasonthebeat/look-at-me-ft-xxxtentacion/likes",
    "https://soundcloud.com/jahseh-onfroy/triumph1/likes",
    "https://soundcloud.com/jahseh-onfroy/kill-my-vibe-feat-tom-g/likes",
    "https://soundcloud.com/kanyewest/heartless/likes",
    "https://soundcloud.com/kanyewest/bound-2/likes",
    "https://soundcloud.com/kanyewest/hurricane/likes",
    "https://soundcloud.com/kanyewest/i-love-it-kanye-west-lil-pump/likes",
    "https://soundcloud.com/kanyewest/all-of-the-lights/likes",
    "https://soundcloud.com/kanyewest/stronger/likes",
    "https://soundcloud.com/kanyewest/off-the-grid/likes",
    "https://soundcloud.com/j-cole/middle-child/likes",
    "https://soundcloud.com/j-cole/power-trip-feat-miguel-1/likes",
    "https://soundcloud.com/j-cole/m-y-l-i-f-e/likes",
    "https://soundcloud.com/j-cole/deja-vu-1/likes",
    "https://soundcloud.com/j-cole/adonis-interlude-the-montage/likes",
    "https://soundcloud.com/j-cole/p-r-i-d-e-i-s-t-h-e-d-e-v-i-l/likes",
    "https://soundcloud.com/j-cole/neighbors-1/likes",
    "https://soundcloud.com/asvpxrocky/praise-the-lord-da-shine-feat/likes",
    "https://soundcloud.com/asvpxrocky/f-kin-problems/likes",
    "https://soundcloud.com/asvpxrocky/sundress/likes",
    "https://soundcloud.com/asvpxrocky/a-ap-forever-feat-moby/likes",
    "https://soundcloud.com/asvpxrocky/a-ap-rocky-shittin-me/likes",
    "https://soundcloud.com/asvpxrocky/fukk-sleep-feat-fka-twigs/likes",
    "https://soundcloud.com/asvpxrocky/fashion-killa/likes",
    "https://soundcloud.com/asvpxrocky/a-ap-rocky-d-m-b-1/likes",
    "https://soundcloud.com/octobersveryown/drake-21-savage-rich-flex/likes",
    "https://soundcloud.com/octobersveryown/drake-21-savage-spin-bout-u/likes",
    "https://soundcloud.com/octobersveryown/drake-knife-talk-feat-21/likes",
    "https://soundcloud.com/octobersveryown/drake-jimmy-cooks-feat-21/likes",
    "https://soundcloud.com/octobersveryown/drake-fair-trade-feat-travis/likes",
    "https://soundcloud.com/octobersveryown/drake-chicago-freestyle/likes",
    "https://soundcloud.com/octobersveryown/drake-jumbotron-shit-poppin/likes",
    "https://soundcloud.com/octobersveryown/drake-wants-and-needs-feat-lil/likes",
    "https://soundcloud.com/octobersveryown/drake-yebba-yebbas-heartbreak/likes",
    "https://soundcloud.com/hykeemcarter/family-ties/likes",
    "https://soundcloud.com/hykeemcarter/orange-soda/likes",
    "https://soundcloud.com/hykeemcarter/honest/likes",
    "https://soundcloud.com/hykeemcarter/trademark-usa/likes",
    "https://soundcloud.com/hykeemcarter/lost-souls-feat-brent-faiyaz/likes",
    "https://soundcloud.com/hykeemcarter/16a1/likes",
    "https://soundcloud.com/hykeemcarter/durag-activity/likes",
    "https://soundcloud.com/hykeemcarter/bank-account-feat-lil-uzi-vert/likes",
    "https://soundcloud.com/hykeemcarter/stats-1/likes",
    "https://soundcloud.com/hykeemcarter/booman/likes",
    "https://soundcloud.com/hykeemcarter/hooligan/likes",
    "https://soundcloud.com/hykeemcarter/vent/likes",
    "https://soundcloud.com/hykeemcarter/range-brothers/likes",
    "https://soundcloud.com/frankocean/pyramids/likes",
    "https://soundcloud.com/frankocean/pink-matter-album-version-feat/likes",
    "https://soundcloud.com/frankocean/super-rich-kids-album-version/likes",
    "https://soundcloud.com/frankocean/sweet-life/likes",
    "https://soundcloud.com/liluzivert/lil-uzi-vert-just-wanna-rock/likes",
    "https://soundcloud.com/liluzivert/drankin-n-smokin/likes",
    "https://soundcloud.com/liluzivert/15-xo-tour-llif3/likes",
    "https://soundcloud.com/liluzivert/20-min-1/likes",
    "https://soundcloud.com/liluzivert/the-way-life-goes/likes",
    "https://soundcloud.com/liluzivert/buy-it-prod-zaytoven/likes",
    "https://soundcloud.com/liluzivert/erase-your-social-produced-by-don-cannon-lyle-leduff/likes",
    "https://soundcloud.com/liluzivert/money-longer-radio-rip/likes",
    "https://soundcloud.com/liluzivert/silly-watch/likes",
    "https://soundcloud.com/liluzivert/sanguine-paradise/likes",
    "https://soundcloud.com/liluzivert/for-fun-prod-by-beatsbyjeff/likes",
    "https://soundcloud.com/liluzivert/you-was-right-produced-by-metro-boomin/likes",
    "https://soundcloud.com/liluzivert/4-7am-produced-by-dp-beatz/likes",
    "https://soundcloud.com/liluzivert/thats-it/likes",
    "https://soundcloud.com/liluzivert/15-luv-scars-ko/likes",
    "https://soundcloud.com/rgsdamedot/balacananas/likes",
    "https://soundcloud.com/rgsdamedot/rich-nigga-summer/likes",
    "https://soundcloud.com/rgsdamedot/something-bout/likes",
    "https://soundcloud.com/rgsdamedot/washed-my-hands/likes",
    "https://soundcloud.com/rgsdamedot/lemme-see/likes",
    "https://soundcloud.com/rgsdamedot/you-gon-think/likes",
    "https://soundcloud.com/rgsdamedot/jamaica/likes",
    "https://soundcloud.com/rgsdamedot/cuban-on/likes",
    "https://soundcloud.com/rgsdamedot/look-at-me-na/likes",
    "https://soundcloud.com/rgsdamedot/zaza/likes",
    "https://soundcloud.com/rgsdamedot/pop-smoke/likes",
    "https://soundcloud.com/rgsdamedot/mandatory/likes",
    "https://soundcloud.com/rgsdamedot/milan/likes",
    "https://soundcloud.com/770rd/lil-yachty-strike-holster/likes",
    "https://soundcloud.com/770rd/nbayoungboat-feat-nba-youngboy/likes",
    "https://soundcloud.com/770rd/poland-lil-yachtyprod-f1lthy/likes",
    "https://soundcloud.com/770rd/yachty-1night-prod-thegoodperry/likes",
    "https://soundcloud.com/770rd/yacht-club-feat-juice-wrld/likes",
    "https://soundcloud.com/770rd/lil-yachty-pardon-me-feat/likes",
    "https://soundcloud.com/770rd/lil-yachty-future-playboi/likes",
    "https://soundcloud.com/770rd/get-dripped-feat-playboi-carti/likes",
    "https://soundcloud.com/770rd/66-feat-trippie-red/likes",
    "https://soundcloud.com/770rd/coffin-lil-yachty/likes",
    "https://soundcloud.com/770rd/lil-yachty-dababy-oprahs-bank/likes",
    "https://soundcloud.com/770rd/lil-yachty-hit-bout-it-feat/likes",
    "https://soundcloud.com/770rd/lil-yachty-split-whole-time/likes",
    "https://soundcloud.com/770rd/lil-yachty-pretty/likes",
    "https://soundcloud.com/770rd/lil-yachty-the-black-seminole/likes",
    "https://soundcloud.com/770rd/lil-yachty-hybrid-feat-baby/likes",
    "https://soundcloud.com/sn0t/gosha/likes",
    "https://soundcloud.com/lilyeat/get-busy-prod-flansie-skimayne/likes",
    "https://soundcloud.com/lilyeat/not-tha-same-prod-clibbo-herres/likes",
    "https://soundcloud.com/lilyeat/mad-bout-that/likes",
    "https://soundcloud.com/sn0t/doja-feat-aap-rocky/likes",
    "https://soundcloud.com/smokepurpp/audi-ii/likes",
    "https://soundcloud.com/smokepurpp/dirty-dirty-feat-lil-skies/likes",
    "https://soundcloud.com/smokepurpp/ski-mask-prod-kendrick/likes",
    "https://soundcloud.com/smokepurpp/123murdabeatz/likes",
    "https://soundcloud.com/smokepurpp/fingers-blue-ft-travis-scott/likes",
    "https://soundcloud.com/smokepurpp/nephew/likes",
    "https://soundcloud.com/sn0t/snot-beretta-ft-wifisfuneral/likes",
    "https://soundcloud.com/sn0t/simple/likes",
    "https://soundcloud.com/sn0t/revenge/likes",
    "https://soundcloud.com/sn0t/06-like-me-feat-iann-dior/likes",
    "https://soundcloud.com/sn0t/moon-stars-ft-maggie-lindemann/likes",
    "https://soundcloud.com/sn0t/whipski-ft-lil-skies-internet-money/likes",
    "https://soundcloud.com/sn0t/mean-feat-flo-milli/likes",
    "https://soundcloud.com/sn0t/immaculate/likes",
    "https://soundcloud.com/sn0t/stranded/likes",
    "https://soundcloud.com/sn0t/ms-porter/likes",
    "https://soundcloud.com/sn0t/human-feat-night-lovell/likes",
    "https://soundcloud.com/smokepurpp/what-i-please-feat-denzel-curry-1/likes",
    "https://soundcloud.com/smokepurpp/dndmurdabeatz/likes",
    "https://soundcloud.com/smokepurpp/glock-inside-my-benz-prod-tm88/likes",
    "https://soundcloud.com/smokepurpp/double/likes",
    "https://soundcloud.com/smokepurpp/audi/likes",
    "https://soundcloud.com/lilyeat/not-sorry-prod-trgc-x-sharkboy/likes",
    "https://soundcloud.com/lilyeat/my-wrist/likes",
    "https://soundcloud.com/lilyeat/already-rich/likes",
    "https://soundcloud.com/lilyeat/myself/likes",
    "https://soundcloud.com/lilyeat/shhhh/likes",
    "https://soundcloud.com/lilyeat/woa/likes",
    "https://soundcloud.com/lilyeat/7-nightz/likes",
    "https://soundcloud.com/lilyeat/demon-tied/likes",
    "https://soundcloud.com/lilyeat/heavyweight/likes",
    "https://soundcloud.com/lilyeat/type-money/likes",
    "https://soundcloud.com/lilyeat/now-feat-luh-geeky/likes",
    "https://soundcloud.com/lilyeat/rav3-p4rty-feat-kranky-kranky/likes",
    "https://soundcloud.com/lilyeat/sum-2-do/likes",
    "https://soundcloud.com/lilyeat/mean-feen-feat-kranky-kranky/likes",
    "https://soundcloud.com/hykeemcarter/the-hillbillies/likes",
    "https://soundcloud.com/lildurk/all-my-life-feat-j-cole/likes",
    "https://soundcloud.com/nba-youngboy/youngboy-never-broke-907596618/likes",
    "https://soundcloud.com/eslabonarmado/eslabon-armado-peso-pluma-ella/likes",
    "https://soundcloud.com/toosii2x/toosii-favorite-song/likes",
    "https://soundcloud.com/lildurk/pelle-coat/likes",
    "https://soundcloud.com/gunna/bread-butter/likes",
    "https://soundcloud.com/youngnudy/peaches-eggplants-feat-21/likes",
    "https://soundcloud.com/pesopluma/bye/likes",
    "https://soundcloud.com/travis-scott-radio/sdp-interlude-demo/likes",
    "https://soundcloud.com/lilmabu/mathematicaldisrespect/likes",
    "https://soundcloud.com/dcorleo/penthouse-shordy-prod-16teen/likes",
    "https://soundcloud.com/metroboomin/metro-boomin-coi-leray-self/likes",
    "https://soundcloud.com/lil-baby-4pf/low-down/likes",
    "https://soundcloud.com/octobersveryown/drake-search-rescue/likes",
    "https://soundcloud.com/unotheactivist-sc/is-you-dumb/likes",
    "https://soundcloud.com/new_genn/ken-carson-lil-yatchy-cant-go/likes",
    "https://soundcloud.com/adam-wiseman-27249415/playboi-carti-locked-in-prod-adam-wiseman/likes",
    "https://soundcloud.com/user-177645440/16-29-throw-it-up-feat-lil-uzi/likes",
    "https://soundcloud.com/camerxxn/ill-never-wear-a-dress-1/likes",
    "https://soundcloud.com/zonesoundzrecords/playboi-carti-designer-shoes/likes",
    "https://soundcloud.com/chezr/used-to-ft-yeat-cheromani/likes",
    "https://soundcloud.com/clumzy-jay/lying-4-fun-second-part-only/likes",
    "https://soundcloud.com/gunna/fukumean/likes",
    "https://soundcloud.com/gunna/back-to-the-moon/likes",
    "https://soundcloud.com/gunna/rodeo-dr/likes",
    "https://soundcloud.com/gunna/back-at-it/likes",
    "https://soundcloud.com/gunna/bottom/likes",
    "https://soundcloud.com/gunna/cah-shit/likes",
    "https://soundcloud.com/gunna/idk-nomore/likes",
    "https://soundcloud.com/gunna/paybach/likes",
    "https://soundcloud.com/gunna/go-crazy/likes",
    "https://soundcloud.com/gunna/p-angels/likes",
]
WEBPAGE_LOAD_TIME = 10


FOLLOWERS_LINKS = [
    "https://soundcloud.com/gunna/followers",
    "https://soundcloud.com/toosii2x/followers",
    "https://soundcloud.com/youngnudy/followers",
    "https://soundcloud.com/metroboomin/followers",
    "https://soundcloud.com/octobersveryown/followers",
    "https://soundcloud.com/770rd/followers/followers",
    "https://soundcloud.com/futureisnow/followers",
    "https://soundcloud.com/ynwmelly/followers",
    "https://soundcloud.com/21savage/followers",
    "https://soundcloud.com/liluzivert/followers",
    "https://soundcloud.com/szababy2/followers",
    "https://soundcloud.com/steevlacy/followers",
    "https://soundcloud.com/summerwalker/followers",
    "https://soundcloud.com/torylanez/followers",
    "https://soundcloud.com/kaliuchis/followers",
    "https://soundcloud.com/brentfaiyaz/followers",
    "https://soundcloud.com/theweeknd/followers",
    "https://soundcloud.com/chris_brown/followers",
    "https://soundcloud.com/brysontiller/followers",
    "https://soundcloud.com/childish-gambino/followers",
    "https://soundcloud.com/roywoodsofficial/followers",
    "https://soundcloud.com/lil_peep/followers",
    "https://soundcloud.com/mac-demarco-official/followers",
    "https://soundcloud.com/greenday/followers",
    "https://soundcloud.com/panicatthedisco/followers",
    "https://soundcloud.com/rlgrime/followers",
    "https://soundcloud.com/crankdatmusic/followers",
    "https://soundcloud.com/gordoszn/followers",
    "https://soundcloud.com/nickraymondg/followers",
    "https://soundcloud.com/slanderofficial/followers",
    "https://soundcloud.com/nghtmre/followers",
    "https://soundcloud.com/lil-baby-4pf/followers",
    "https://soundcloud.com/youngthugworld/followers",
    "https://soundcloud.com/superduperkylemusic/followers",
    "https://soundcloud.com/lil-skies/followers",
    "https://soundcloud.com/dabilliondollarbaby/followers",
    "https://soundcloud.com/nlechoppa/followers",
    "https://soundcloud.com/jaydayoungan/followers",
    "https://soundcloud.com/jackharlow/followers",
    "https://soundcloud.com/postmalone/followers",
    "https://soundcloud.com/pnbrock/followers",
    "https://soundcloud.com/polo-g/followers",
    "https://soundcloud.com/biggavelipro/followers",
    "https://soundcloud.com/trippie-hippie-2/followers",
    "https://soundcloud.com/liluzivert/followers",
    "https://soundcloud.com/travisscott-2/followers",
    "https://soundcloud.com/danielcaesar/followers",
    "https://soundcloud.com/migosatl/followers",
    "https://soundcloud.com/mustardofficial/followers",
    "https://soundcloud.com/roddyricch/followers",
    "https://soundcloud.com/rodwave/followers",
    "https://soundcloud.com/raesremmurd/followers",
    "https://soundcloud.com/uiceheidd/followers",
    "https://soundcloud.com/comethazine/followers",
    "https://soundcloud.com/lilmosey/followers",
    "https://soundcloud.com/ygravy/followers",
    "https://soundcloud.com/youngthugworld/followers",
    "https://soundcloud.com/nba-youngboy/followers",
    "https://soundcloud.com/a-boogie-wit-da-hoodie/followers",
]


def soundcloud_url_finder_main_loop_2(driver):
    driver.get(random.choice(FOLLOWERS_LINKS))
    wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # load page
    loading_start_time = time.time()
    time_waiting = 0
    while time_waiting < WEBPAGE_LOAD_TIME:
        scroll_to_bottom(driver)
        time_waiting = time.time() - loading_start_time

    # read names
    names = find_names(driver)

    # convert names to soundcloud link
    links = convert_names_to_soundcloud_link(names)

    # write names to file
    writes = write_links_to_file(links)

    return writes


def soundcloud_url_finder_main_loop(driver):
    # get to random song's likes page
    webpage_loading_start_time = time.time()
    driver.get(random.choice(LIKES_LINKS))

    # Wait for the webpage to load
    wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # load page
    loading_start_time = time.time()
    time_waiting = 0
    while time_waiting < WEBPAGE_LOAD_TIME:
        scroll_to_bottom(driver)
        time_waiting = time.time() - loading_start_time

    # read names
    names = find_names(driver)

    # convert names to soundcloud link
    links = convert_names_to_soundcloud_link(names)

    # write names to file
    writes = write_links_to_file(links)

    return writes


def write_links_to_file(links):
    writes = 0
    for link in links:
        append_method_return = append_to_raw_links_file(link)
        if (
            append_method_return != "Line already exists in file"
            and append_method_return != "Error writing to file"
        ):
            writes += 1
    return writes


def convert_names_to_soundcloud_link(names):
    links = []
    for n in names:
        links.append(convert_name_to_soundcloud_link(n))
    return links


def convert_name_to_soundcloud_link(name):
    # replace spaces with dashes
    parsed_name = ""
    for char in name:
        if char == " ":
            parsed_name += "-"
        else:
            parsed_name += char

    # assemble and return link
    return "https://soundcloud.com/" + parsed_name


# LIKES_LINKS debug methods
def check_for_dupes_in_likes_links(list):
    seen = set()
    duplicates = set()

    for link in list:
        if link in seen:
            duplicates.add(link)
        else:
            seen.add(link)

    for duplicate in duplicates:
        print(duplicate)


def check_for_invalid_likes_links(list):
    bad_urls = []

    for url in list:
        url_parts = url.split("/")

        if len(url_parts) != 6:
            bad_urls.append(url)
            continue

        if url_parts[0] != "https:":
            bad_urls.append(url)
            continue

        if "soundcloud.com" not in url_parts[2]:
            bad_urls.append(url)
            continue

        if url_parts[5] != "likes":
            bad_urls.append(url)
            continue

    print("-------------------------------------------")
    for bad_url in bad_urls:
        print(bad_url)

    print(f"There are {len(bad_urls)} invalids")
    print("-------------------------------------------")


def check_for_invalid_follower_links(list):
    bad_links = []
    for item in list:
        if "https://soundcloud.com/" not in item:
            bad_links.append(item)
            continue

        elif "followers" not in item:
            bad_links.append(item)
            continue

        elif len(item.split("/")) != 5:
            bad_links.append(item)
            continue

    for item in bad_links:
        print(item)
    print(f"There are {len(bad_links)} bad links")
