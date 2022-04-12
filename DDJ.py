import requests
from bs4 import BeautifulSoup
from os.path import exists
import json


def get_recent_episode_nr():
    page = requests.get("https://darknetdiaries.com/")
    page_soup = BeautifulSoup(page.text, "html.parser")

    sixth_a = page_soup.findAll('a')[5]
    last_episode_title = sixth_a.text

    nr_end = last_episode_title.find(':')
    recent_episode_str = last_episode_title[3:nr_end]

    return int(recent_episode_str)


#  json_data - reading json data from extracted string (script)
#  json_py_dict - empty python dictionary ready to be updated in each iteration
#  json_dump_str - dumped json string from python dictionary (json_py_dict) waiting to be written to a file

recent_episode_nr = get_recent_episode_nr()  # TODO ConnectionError exception


def create_json(episode_numbers=range(1, recent_episode_nr + 1, 1)):
    if type(episode_numbers) is list:
        with open("DD.json") as json_file:
            json_py_dict = json.load(json_file)
    else:
        json_py_dict = dict()

    for i in episode_numbers:
        url = "https://darknetdiaries.com/episode/0/"
        url = url.replace("0", str(i))

        page = requests.get(url)
        page_soup = BeautifulSoup(page.text, "html.parser")

        scripts = page_soup.findAll("script")
        script = str(scripts[3])
        script = script.replace("<script>", '', 1)
        script = script.replace("window.playerConfiguration = ", '', 1)
        script = script.replace("</script>", '', 1)
        json_data = json.loads(script)

        title = json_data["episode"]["title"]
        title = title.replace(':', '')

        link = json_data["episode"]["media"]["mp3"]

        print('"' + str(i) + '": {"title": "' + title + '", "link": "' + link + '"}')

        json_py_dict.update({str(i): {"title": title, "link": link}})

    json_dumped_str = json.dumps(json_py_dict, indent=4)

    with open("DD.json", 'wt') as json_file:
        json_file.write(json_dumped_str)
    print("\nFile exported successfully.")


def check_json():
    with open("DD.json") as json_file:
        json_py_dict = json.load(json_file)

    missing_entries = []
    for i in range(1, recent_episode_nr + 1):

        if json_py_dict.get(str(i)) is None or json_py_dict.get(str(i)).get("title") is None or json_py_dict.get(
                str(i)).get("link") is None:
            print(f"Error - missing entry on {i} episode.")
            missing_entries.append(i)

    return missing_entries


def check_file():
    episode_numbers = check_json()
    if not exists("DD.json"):
        print("DD.json not found, creating a brand new file...")
        create_json()

    elif episode_numbers:
        print("Corrupted DD.json found, appending new entries...")
        create_json(episode_numbers)

    else:
        print("Intact DD.json found, proceeding...")


if __name__ == "__main__":
    check_file()
