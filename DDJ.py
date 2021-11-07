import requests
from bs4 import BeautifulSoup
from os.path import exists, getsize
from alive_progress import alive_bar
import json

#  json_data - reading json data from extracted string (script)
#  json_py_dict - empty python dictionary ready to be updated in each iteration
#  json_dump_str - dumped json string from python dictionary (json_py_dict) waiting to be written to a file


def create_json():
    json_py_dict = dict()
    recent_episode_nr = 103

    with alive_bar(recent_episode_nr, title="Generating...", bar="filling", length=40, spinner="waves") as bar:
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
            bar.text(title)

            link = json_data["episode"]["media"]["mp3"]

            json_py_dict.update({str(i): {"title": title, "link": link}})

            bar()

    json_dumped_str = json.dumps(json_py_dict, indent=4)

    with open("DD.json", 'wt') as f:
        f.write(json_dumped_str)
    print("\nFile exported successfully.")


def check_file():
    if not exists("DD.json"):
        print("DD.json not found, creating a brand new file...")
        create_json()
    elif getsize("DD.json") != 14660:
        print("Corrupted DD.json found, creating a brand new file...")
        create_json()
    else:
        print("Intact DD.json found, proceeding...")


if __name__ == "__main__":
    check_file()
