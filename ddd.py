import json
import argparse
import requests
import ddj


def episode_int(str_num):
    print(str_num)
    int_num = int(str_num)
    if int_num <= 0 or int_num > ddj.recent_episode_nr:
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
    default=ddj.recent_episode_nr,
    type=episode_int,
    help=f"Ends downloading to number. (int) (default={ddj.recent_episode_nr})",
    dest="end",
)
parser.add_argument(
    "-c",
    "--choices",
    nargs="+",
    default=range(1, ddj.recent_episode_nr + 1, 1),
    type=episode_int,
    help=f"""Gets any int arguments and then downloads them. (list[int])
    (default=1..{ddj.recent_episode_nr})""",
)
args = parser.parse_args()


def download_podcast():
    with open("dd.json", "rt", encoding="utf-8") as json_file:
        json_py_dict = json.load(json_file)

    from_to = args.choices if args.choices else range(args.start, args.end + 1, 1)
    print("\nDownloading started...")
    for i in from_to:
        link = json_py_dict[str(i)]["link"]
        title = json_py_dict[str(i)]["title"]

        print(title + ": " + link)

        episode = requests.get(link)

        with open(title + ".mp3", "wb") as local_file:
            local_file.write(episode.content)


if __name__ == "__main__":
    ddj.check_file()
    download_podcast()
