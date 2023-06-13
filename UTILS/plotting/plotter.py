import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

def create_data_graph():
    file_path = r"C:\Users\matt\AppData\Roaming\py-soundcloud-follower\user_data.txt"
    html_path = r"C:\Users\matt\AppData\Roaming\py-soundcloud-follower\graph_image\data_image.html"

    # Read the data file into a pandas DataFrame
    df = pd.read_csv(file_path, delimiter="///", header=None, names=["DateTime", "Followers", "Following"])

    # Convert the DateTime column to datetime type
    df["DateTime"] = pd.to_datetime(df["DateTime"])

    # Create a subplot with two y-axes
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces for Followers and Following
    fig.add_trace(
        px.line(df, x="DateTime", y="Followers", color_discrete_sequence=["blue"]).data[0],
        secondary_y=False,
    )

    fig.add_trace(
        px.line(df, x="DateTime", y="Following", color_discrete_sequence=["orange"]).data[0],
        secondary_y=True,
    )

    # Set axis labels
    fig.update_xaxes(title_text="DateTime")
    fig.update_yaxes(title_text="Followers", secondary_y=False)
    fig.update_yaxes(title_text="Following", secondary_y=True)

    # Save the graph as an HTML file
    fig.write_html(html_path)
