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
    recent_episode_nr = int(recent_episode_str)

    return recent_episode_nr

#  json_data - reading json data from extracted string (script)
#  json_py_dict - empty python dictionary ready to be updated in each iteration
#  json_dump_str - dumped json string from python dictionary (json_py_dict) waiting to be written to a file


def create_json():
    json_py_dict = dict()
    recent_episode_nr = get_recent_episode_nr()

    for i in range(1, recent_episode_nr + 1, 1):
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

    with open("DD.json", 'wt') as f:
        f.write(json_dumped_str)
    print("\nFile exported successfully.")


def check_json():
    recent_episode_nr = get_recent_episode_nr()

    with open("DD.json") as f:
        json_py_dict = json.load(f)

    for i in range(1, recent_episode_nr + 1):

        if json_py_dict.get(str(i)) is None or json_py_dict.get(str(i)).get("title") is None or json_py_dict.get(str(i)).get("link") is None:
            print(f"Error - missing entry on {i} episode.")
            return True

    return False


def check_file():
    if not exists("DD.json"):
        print("DD.json not found, creating a brand new file...")
        create_json()

    elif check_json():
        print("Corrupted DD.json found, creating a brand new file...")
        create_json()

    else:
        print("Intact DD.json found, proceeding...")


if __name__ == "__main__":
    check_file()
