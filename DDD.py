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
                    help="Starts downloading from this episode number. (int) (default=1)", dest="start")
parser.add_argument(nargs='?', default=DDJ.recent_episode_nr, type=episode_int,
                    help="Ends downloading to number. (int) (default=recent_episode_number)", dest="end")
args = parser.parse_args()


def download_podcast():
    with open("DD.json") as f:
        json_py_dict = json.load(f)

    print("\nDownloading started...")
    for i in range(args.start, args.end + 1, 1):
        link = json_py_dict[str(i)]["link"]
        title = json_py_dict[str(i)]["title"]

        print(title + ': ' + link)

        episode = requests.get(link)

        with open(title + ".mp3", 'wb') as local_file:
            local_file.write(episode.content)


if __name__ == "__main__":
    DDJ.check_file()
    download_podcast()
