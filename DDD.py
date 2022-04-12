import DDJ
import requests
import json
import argparse


def episode_int(n):
    n = int(n)
    if n <= 0 or n > DDJ.recent_episode_nr:
        raise argparse.ArgumentTypeError("Episode number out of range!")
    return n


parser = argparse.ArgumentParser(prog="Darknet Diaries Downloader")
parser.add_argument(nargs='?', default=1, type=episode_int,
                    help="starts downloading from this episode number. (int) (default=1)", dest="start")
parser.add_argument(nargs='?', default=DDJ.recent_episode_nr, type=episode_int,
                    help=f"ends downloading to number. (int) (default={DDJ.recent_episode_nr})", dest="end")
parser.add_argument('-c', "--choices", nargs='+', default=range(1, DDJ.recent_episode_nr + 1, 1), type=episode_int,
                    help=f"gets any int arguments and then downloads them. (list_with_ints) (default=1..{DDJ.recent_episode_nr})")
args = parser.parse_args()


def download_podcast():
    with open("DD.json") as json_file:
        json_py_dict = json.load(json_file)

    from_to = args.choices if args.choices else range(args.start, args.end + 1, 1)
    print("\nDownloading started...")
    for i in from_to:
        link = json_py_dict[str(i)]["link"]
        title = json_py_dict[str(i)]["title"]

        print(title + ': ' + link)

        episode = requests.get(link)

        with open(title + ".mp3", 'wb') as mp3_file:
            mp3_file.write(episode.content)


if __name__ == "__main__":
    DDJ.check_file()
    download_podcast()
