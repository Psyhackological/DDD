"""
Darknet Diaries Downloader
Fetches and downloads episodes from Darknet Diaries using specified episode numbers.
"""

import argparse
import os

import requests


def fetch_podcast_links(url):
    """Fetch podcast links from the given URL and return them as a list."""
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the data.")
        return []
    return response.text.strip().split("\n")


def download_podcast(episode_url, dest_folder="podcasts"):
    """Download a podcast episode and save it to a specified folder."""
    filename = episode_url.split("/")[-1]
    filepath = os.path.join(dest_folder, filename)

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    response = requests.get(episode_url, stream=True)
    if response.status_code != 200:
        print(f"Failed to download {episode_url}")
        return

    with open(filepath, "wb") as file_handle:
        for chunk in response.iter_content(chunk_size=8192):
            file_handle.write(chunk)


def get_recent_episode_nr():
    """Get the most recent episode number."""
    url = "https://darknetdiaries.com/darknet-diaries-all-episode-links.txt"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the data.")
        return 0
    return len(response.text.strip().split("\n"))


RECENT_EPISODE_NR = get_recent_episode_nr()


def episode_int(str_num):
    """Convert string to integer and check if it's a valid episode number."""
    int_num = int(str_num)
    if int_num <= 0 or int_num > RECENT_EPISODE_NR:
        raise argparse.ArgumentTypeError("Episode number out of range!")
    return int_num


PARSER = argparse.ArgumentParser(
    prog="Darknet Diaries Downloader",
    description="Starts downloading from this episode number.",
)
PARSER.add_argument(
    nargs="?",
    default=1,
    type=episode_int,
    help="Starts downloading from this episode number. (int) (default=1)",
    dest="start",
)
PARSER.add_argument(
    nargs="?",
    default=RECENT_EPISODE_NR,
    type=episode_int,
    help="Ends downloading to number. (int)",
    dest="end",
)
PARSER.add_argument(
    "-c",
    "--choices",
    nargs="+",
    default=range(1, RECENT_EPISODE_NR + 1),
    type=episode_int,
    help="Gets any int arguments and then downloads them. (list[int])",
)

ARGS = PARSER.parse_args()


def main():
    """Main function to handle downloading."""
    url = "https://darknetdiaries.com/darknet-diaries-all-episode-links.txt"
    episodes = fetch_podcast_links(url)
    from_to = ARGS.choices if ARGS.choices else range(ARGS.start, ARGS.end + 1)

    print("\nDownloading started...")
    for idx in from_to:
        episode_url = episodes[idx - 1]
        print(f"Downloading {idx}. {episode_url}")
        download_podcast(episode_url)


if __name__ == "__main__":
    main()
