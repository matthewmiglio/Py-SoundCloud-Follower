import os


def create_upper_folder():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")
    os.makedirs(folder_path, exist_ok=True)


def create_links_text_file():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")
    file_path = os.path.join(folder_path, "soundcloud-links.txt")
    open(file_path, "a").close()


def upper_folder_exists():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")
    return os.path.exists(folder_path)


def links_text_file_exists():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")
    file_path = os.path.join(folder_path, "soundcloud-links.txt")
    return os.path.exists(file_path)


def append_to_links_file(line):
    try:
        folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")
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


def remove_and_return_oldest_links_line():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")
    file_path = os.path.join(folder_path, "soundcloud-links.txt")
    with open(file_path, "r+") as file:
        lines = file.readlines()
        oldest_line = lines.pop(0).strip() if lines else None
        file.seek(0)
        file.truncate()
        file.writelines(lines)
    return oldest_line


def create_good_links_file():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")
    file_path = os.path.join(folder_path, "good_links.txt")
    open(file_path, "a").close()


def good_links_file_exists():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")
    file_path = os.path.join(folder_path, "good_links.txt")
    return os.path.exists(file_path)


def add_to_good_links(line):
    try:
        folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")
        file_path = os.path.join(folder_path, "good_links.txt")

        with open(file_path, "a") as file:
            file.write(line + "\n")
    except:
        return "Error writing to file"


def get_good_links_line_count():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")
    file_path = os.path.join(folder_path, "good_links.txt")
    with open(file_path, "r") as file:
        lines = file.readlines()
    return len(lines)


def get_soundcloud_links_line_count():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")
    file_path = os.path.join(folder_path, "soundcloud-links.txt")
    with open(file_path, "r") as file:
        lines = file.readlines()
    return len(lines)


def return_and_delete_last_line_in_good_urls():
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")
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
    folder_path = os.path.join(os.getenv("APPDATA"), "py-soundcloud-follower")
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


def create_user_data_file():
    file_path = os.path.join(
        os.getenv("APPDATA"), "py-soundcloud-follower", "user_data.txt"
    )
    open(file_path, "w").close()


def user_data_file_exists():
    file_path = os.path.join(
        os.getenv("APPDATA"), "py-soundcloud-follower", "user_data.txt"
    )
    return os.path.exists(file_path)


def read_user_data_file():
    file_path = os.path.join(
        os.getenv("APPDATA"), "py-soundcloud-follower", "user_data.txt"
    )
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def append_to_user_data_file(line):
    file_path = os.path.join(
        os.getenv("APPDATA"), "py-soundcloud-follower", "user_data.txt"
    )
    with open(file_path, "a") as file:
        file.write(line + "\n")


print(
    f"-----------------------------------------------\n-----------------------------------------------\nFile system setup:"
)

if not user_data_file_exists():
    create_user_data_file()

if not good_links_file_exists():
    create_good_links_file()

if not upper_folder_exists():
    create_upper_folder()

if not links_text_file_exists():
    create_links_text_file()

print(
    f"Removed {remove_duplicate_lines_from_good_links()} duplicate lines from good links file"
)
print(
    f"File system setup complete\n-----------------------------------------------\n-----------------------------------------------"
)
