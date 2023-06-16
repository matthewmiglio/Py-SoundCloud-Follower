from selenium import webdriver
import time


import os
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots


def create_data_graph():
    start_time = time.time()
    print("Making plot...")

    appdata_dir = os.environ.get("APPDATA")

    file_path = os.path.join(appdata_dir, "py-soundcloud-follower", "user_data.txt")

    html_path = os.path.join(
        appdata_dir, "py-soundcloud-follower", "graph_image", "data_image.html"
    )

    # create the graph image as html
    html_image_start_time = time.time()

    # Read the data file into a pandas DataFrame
    data_read_start_time = time.time()
    df = pd.read_csv(
        file_path,
        delimiter="///",
        header=None,
        names=["DateTime", "Followers", "Following"],
    )

    # Convert the DateTime column to datetime type
    df["DateTime"] = pd.to_datetime(df["DateTime"])
    # print(f"Took {str(time.time() - data_read_start_time)[:5]} seconds to read data")

    # Create a subplot with two y-axes
    subplots_start_time = time.time()
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces for Followers and Following
    fig.add_trace(
        px.line(df, x="DateTime", y="Followers", color_discrete_sequence=["blue"]).data[
            0
        ],
        secondary_y=False,
    )

    fig.add_trace(
        px.line(
            df, x="DateTime", y="Following", color_discrete_sequence=["orange"]
        ).data[0],
        secondary_y=True,
    )

    # Set axis labels
    fig.update_xaxes(title_text="DateTime")
    fig.update_yaxes(title_text="Followers", secondary_y=False)
    fig.update_yaxes(title_text="Following", secondary_y=True)

    # print(
    #     f"Took {str(time.time()-subplots_start_time)[:5]} seconds to add subplots and axies"
    # )

    # print(
    #     f"Took {str(time.time()-html_image_start_time)[:5]} seconds to create the graph image as html"
    # )

    # Save the graph as an HTML file
    save_image_start_time = time.time()
    fig.write_html(html_path)
    # print(
    #     f"Took {str(time.time() - save_image_start_time)[:5]} seconds to save HTML image"
    # )

    # convert the html file to png
    convert_time_start_time = time.time()
    html_to_png()
    # print(
    #     f"Took {str(time.time() - convert_time_start_time)[:5]} seconds to convert HTML image to png"
    # )

    print(
        f"Took {str(time.time() - start_time)[:5]} seconds total to create plot image"
    )
    print(
        "-----------------------------------------------\n-----------------------------------------------"
    )


def html_to_png():
    appdata_dir = os.getenv("APPDATA")
    html_file_path = os.path.join(
        appdata_dir, "py-soundcloud-follower", "graph_image", "data_image.html"
    )
    output_file_path = os.path.join(
        appdata_dir, "py-soundcloud-follower", "graph_image", "data_image.png"
    )
    # Set up the Selenium driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)

    # Load the HTML file
    driver.get("file://" + html_file_path)

    # Wait for the page to load completely (adjust the sleep time if needed)
    time.sleep(1)

    # Capture a screenshot of the loaded page
    driver.save_screenshot(output_file_path)

    # Quit the driver
    driver.quit()
