import os

import PySimpleGUI as sg

from RAW_SOUNDCLOUD_URL_FINDER.main_url_finder import url_finding_main
from USER_DATA_READER.read_user_data import record_user_data
from USER_FOLLOWER.main_follower import follow_main
from UTILS.file_handler import (
    file_setup,
    get_good_links_count,
    get_raw_links_count,
)
from UTILS.plotting.plotter import create_data_graph
from RAW_URL_CHECKER.url_checker import check_one_unchecked_link
from UTILS.file_handler import remove_and_return_random_raw_link
from UTILS.file_handler import remove_line_from_file
from RAW_URL_CHECKER.url_checker import check_one_unchecked_link_wrapper

SOUNDCLOUD_RAW_LINKS_UPPER_LIMIT = 1000

# get program data
good_url_count = get_good_links_count()
raw_url_count = get_raw_links_count()

# get image_pat
appdata_dir = os.environ.get("APPDATA")
image_path = os.path.join(
    appdata_dir, "py-soundcloud-follower", "graph_image", "data_image.png"  # type: ignore
)


# GUI layout
layout = [
    [
        [
            sg.Frame(
                "Target URLs",
                [
                    [
                        sg.Text(
                            f"Good URL Count: {good_url_count}", font=("Helvetica", 14)
                        )
                    ],
                    [
                        sg.Text(
                            f"Raw URL Count: {raw_url_count}", font=("Helvetica", 14)
                        )
                    ],
                    [sg.Text(f"Select Worker Count:", font=("Helvetica", 14))],
                    [
                        sg.Slider(
                            range=(1, 10),
                            default_value=6,
                            orientation="h",
                            size=(30, 20),
                            key="WORKER_COUNT",
                            font=("Helvetica", 14),
                        )
                    ],
                    [sg.Button("Get More Links", size=(15, 2), font=("Helvetica", 14))],
                ],
                element_justification="center",
            )
        ],
        [
            sg.Frame(
                "Following",
                [
                    [sg.Text("Follow Users", font=("Helvetica", 14))],
                    [
                        sg.Slider(
                            range=(5, 100),
                            default_value=5,
                            orientation="h",
                            size=(30, 20),
                            key="-SLIDER-",
                            font=("Helvetica", 14),
                        )
                    ],
                    [sg.Button("Follow Users", size=(15, 2), font=("Helvetica", 14))],
                ],
                element_justification="center",
            )
        ],
    ],
    [
        sg.Frame(
            "Image",
            [
                [sg.Image(filename=image_path)],
            ],
            element_justification="center",
        )
    ],
]


def gui():
    # Create the window
    window = sg.Window("Soundcloud Follower", layout, finalize=True)

    # Event loop
    while True:
        event, values = window.read()  # type: ignore
        if event == sg.WINDOW_CLOSED:
            break

        elif event == "Get More Links":
            worker_count = int(values["WORKER_COUNT"])

            url_finding_main(SOUNDCLOUD_RAW_LINKS_UPPER_LIMIT, worker_count)

        elif event == "Follow Users":
            follow_count = values["-SLIDER-"]
            follow_main(follow_count)

    # Close the window and quit the application
    window.close()


def dummy_main():
    create_data_graph()


if __name__ == "__main__":
    file_setup()
    create_data_graph()
    gui()

    # import concurrent.futures
    # with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    #     futures = []
    #     for _ in range(8):
    #         futures.append(executor.submit(check_one_unchecked_link_wrapper))

    #     # Wait for all threads to complete
    #     concurrent.futures.wait(futures)
