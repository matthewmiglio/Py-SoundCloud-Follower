import PySimpleGUI as sg

from file_handler import get_good_links_line_count, get_soundcloud_links_line_count
from main_follower import follow_main
from main_url_finder import url_finding_main

good_url_count = get_good_links_line_count()
raw_url_count = get_soundcloud_links_line_count()

layout = [
    [
        sg.Frame(
            "Target URLs",
            [
                [sg.Text(f"Good URL Count: {good_url_count}", font=("Helvetica", 14))],
                [sg.Text(f"Raw URL Count: {raw_url_count}", font=("Helvetica", 14))],
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
]


# Create the window
window = sg.Window("Soundcloud Follower", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    elif event == "Get More Links":
        url_finding_main()

    elif event == "Follow Users":
        follow_count = values["-SLIDER-"]
        follow_main(follow_count)


# Close the window
window.close()