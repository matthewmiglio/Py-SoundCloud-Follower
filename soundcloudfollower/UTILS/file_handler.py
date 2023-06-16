from PIL import Image

import os


# main file setup function
def file_setup():
    print(
        f"-----------------------------------------------\n-----------------------------------------------\nFile system setup:"
    )

    # graph image folder
    if not graph_image_folder_exists():
        create_graph_image_folder()

    # user_data.txt file (user statistics text file)
    if not user_data_file_exists():
        create_user_data_file()

    # good_links.txt file (list of soundcloud urls to pages that passed all tests)
    if not good_links_file_exists():
        create_good_links_file()

    # py-soundcloud-follower folder in appdata dir
    if not upper_folder_exists():
        create_upper_folder()

    # soundcloud-links.txt file (stores raw (unchecked) soundcloud profile links)
    if not raw_links_text_file_exists():
        create_raw_links_text_file()

    print(
        f"Removed {remove_duplicate_lines_from_raw_soundcloud_links()} duplicate lines from raw links file"
    )
    print(
        f"Removed {remove_duplicate_lines_from_good_links()} duplicate lines from good links file"
    )
    print(
        f"File system setup complete\n-----------------------------------------------\n-----------------------------------------------"
    )


# main directory


def create_upper_folder():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")  # type: ignore
    os.makedirs(folder_path, exist_ok=True)
    print('Created folder "py-soundcloud-follower" in AppData')


def upper_folder_exists():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")  # type: ignore
    return os.path.exists(folder_path)


# raw links file methods


def create_raw_links_text_file():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")  # type: ignore
    file_path = os.path.join(folder_path, "soundcloud-links.txt")
    open(file_path, "a").close()
    print('Created file "soundcloud-links.txt" in AppData')


def raw_links_text_file_exists():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")  # type: ignore
    file_path = os.path.join(folder_path, "soundcloud-links.txt")
    return os.path.exists(file_path)


def append_to_raw_links_file(line):
    try:
        folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")  # type: ignore
        file_path = os.path.join(folder_path, "soundcloud-links.txt")

        with open(file_path, "r") as file:
            lines = file.readlines()

        # Check if line already exists in the file
        if line + "\n" in lines:
            return "Line already exists in file"

        with open(file_path, "a") as file:
            file.write(line + "\n")
    except:
        return "Error writing to file"


def remove_and_return_oldest_raw_link():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")  # type: ignore
    file_path = os.path.join(folder_path, "soundcloud-links.txt")
    with open(file_path, "r+") as file:
        lines = file.readlines()
        oldest_line = lines.pop(0).strip() if lines else None
        file.seek(0)
        file.truncate()
        file.writelines(lines)
    return oldest_line


def get_raw_links_count():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")  # type: ignore
    file_path = os.path.join(folder_path, "soundcloud-links.txt")
    with open(file_path, "r") as file:
        lines = file.readlines()
    return len(lines)


def remove_duplicate_lines_from_raw_soundcloud_links():
    file_path = os.path.join(
        os.getenv("APPDATA"), "py-soundcloud-follower", "soundcloud-links.txt"  # type: ignore
    )

    lines = set()
    duplicates = set()

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line in lines:
                duplicates.add(line)
            else:
                lines.add(line)

    with open(file_path, "w") as file:
        file.writelines(line + "\n" for line in lines)

    num_duplicates_deleted = len(duplicates)
    return num_duplicates_deleted


# good links file methods


def create_good_links_file():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")  # type: ignore
    file_path = os.path.join(folder_path, "good_links.txt")
    open(file_path, "a").close()
    print('Created file "good_links.txt" in AppData')


def good_links_file_exists():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")  # type: ignore # type: ignore
    file_path = os.path.join(folder_path, "good_links.txt")
    return os.path.exists(file_path)


def add_to_good_links(line):
    try:
        folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")  # type: ignore
        file_path = os.path.join(folder_path, "good_links.txt")

        with open(file_path, "a") as file:
            file.write(line + "\n")
    except:
        return "Error writing to file"


def get_good_links_count():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")  # type: ignore
    file_path = os.path.join(folder_path, "good_links.txt")
    with open(file_path, "r") as file:
        lines = file.readlines()
    return len(lines)


def return_and_delete_last_line_in_good_urls():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")  # type: ignore
    file_path = os.path.join(folder_path, "good_links.txt")

    with open(file_path, "r+") as file:
        lines = file.readlines()
        if lines:
            last_line = lines.pop().strip()
            file.seek(0)
            file.truncate()
            file.writelines(lines)
            return last_line
        else:
            return None


def remove_duplicate_lines_from_good_links():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")  # type: ignore
    file_path = os.path.join(folder_path, "good_links.txt")

    lines = set()
    duplicates = set()

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line in lines:
                duplicates.add(line)
            else:
                lines.add(line)

    with open(file_path, "w") as file:
        file.writelines(line + "\n" for line in lines)

    num_duplicates_deleted = len(duplicates)
    return num_duplicates_deleted


# user data file methods


def create_user_data_file():
    file_path = os.path.join(
        os.getenv("APPDATA"), "py-soundcloud-follower", "user_data.txt"  # type: ignore
    )
    open(file_path, "w").close()
    print('Created file "user_data.txt" in AppData')


def user_data_file_exists():
    file_path = os.path.join(
        os.getenv("APPDATA"), "py-soundcloud-follower", "user_data.txt"  # type: ignore
    )
    return os.path.exists(file_path)


def read_user_data_file():
    file_path = os.path.join(
        os.getenv("APPDATA"), "py-soundcloud-follower", "user_data.txt"  # type: ignore
    )
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def append_to_user_data_file(line):
    file_path = os.path.join(
        os.getenv("APPDATA"), "py-soundcloud-follower", "user_data.txt"  # type: ignore
    )
    with open(file_path, "a") as file:
        file.write(line + "\n")


# graph image methods


def create_graph_image_folder():
    folder_path = os.path.join(
        os.getenv("APPDATA"), "py-soundcloud-follower", "graph_image"  # type: ignore
    )
    os.makedirs(folder_path, exist_ok=True)
    print('Created folder "graph_image" in AppData')


def graph_image_folder_exists():
    folder_path = os.path.join(
        os.getenv("APPDATA"), "py-soundcloud-follower", "graph_image"  # type: ignore
    )
    return os.path.exists(folder_path)


def check_if_graph_image_file_exists():
    path = os.path.join(
        os.getenv("APPDATA"), "py-soundcloud-follower", "graph_image", "data_plot.png"  # type: ignore
    )
    return os.path.exists(path)


def create_empty_graph__image_file(file_path, width, height):
    image = Image.new("RGB", (width, height), color=(0, 0, 0))
    image.save(file_path)
    print('Created file "data_plot.png" in AppData')
