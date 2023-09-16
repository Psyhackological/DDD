import argparse
import os

import requests


def fetch_podcast_links(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the data.")
        return []
    return response.text.strip().split("\n")


def download_podcast(episode_url, dest_folder="podcasts"):
    filename = episode_url.split("/")[-1]
    filepath = os.path.join(dest_folder, filename)

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    response = requests.get(episode_url, stream=True)
    if response.status_code != 200:
        print(f"Failed to download {episode_url}")
        return

    with open(filepath, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)


def get_recent_episode_nr():
    url = "https://darknetdiaries.com/darknet-diaries-all-episode-links.txt"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the data.")
        return 0
    return len(response.text.strip().split("\n"))


recent_episode_nr = get_recent_episode_nr()


def episode_int(str_num):
    int_num = int(str_num)
    if int_num <= 0 or int_num > recent_episode_nr:
        raise argparse.ArgumentTypeError("Episode number out of range!")
    return int_num


parser = argparse.ArgumentParser(prog="Darknet Diaries Downloader")
parser.add_argument(
    nargs="?",
    default=1,
    type=episode_int,
    help="Starts downloading from this episode number. (int) (default=1)",
    dest="start",
)
parser.add_argument(
    nargs="?",
    default=recent_episode_nr,
    type=episode_int,
    help=f"Ends downloading to number. (int) (default={recent_episode_nr})",
    dest="end",
)
parser.add_argument(
    "-c",
    "--choices",
    nargs="+",
    default=range(1, recent_episode_nr + 1),
    type=episode_int,
    help=f"Gets any int arguments and then downloads them. (list[int]) (default=1..{recent_episode_nr})"
)

args = parser.parse_args()


def main():
    url = "https://darknetdiaries.com/darknet-diaries-all-episode-links.txt"
    episodes = fetch_podcast_links(url)
    from_to = args.choices if args.choices else range(args.start, args.end + 1)

    print("\nDownloading started...")
    for i in from_to:
        episode_url = episodes[i-1]
        print(f"Downloading {i}. {episode_url}")
        download_podcast(episode_url)


if __name__ == "__main__":
    main()
