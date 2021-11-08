import DDJ
import requests
import json


def download_podcast():
    try:
        start = int(input("Start downloading from Episode: "))
        end = int(input("End downloading to Episode (including this number): "))
    except ValueError as e:
        print(f"ValueError: Input needs to be int: {str(e)}")
        exit()

    with open("DD.json") as f:
        json_py_dict = json.load(f)

    print("\nDownloading started...")
    for i in range(start, end + 1, 1):
        link = json_py_dict[str(i)]["link"]
        title = json_py_dict[str(i)]["title"]

        print(title + ': ' + link)

        episode = requests.get(link)

        with open(title + ".mp3", 'wb') as local_file:
            local_file.write(episode.content)


if __name__ == "__main__":
    DDJ.check_file()
    download_podcast()
