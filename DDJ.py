from requests import get
from bs4 import BeautifulSoup
import json
from os.path import exists, getsize


def create_json():
    json_ddd = dict()
    recent_episode_nr = 103
    for i in range(1, recent_episode_nr + 1, 1):
        url = "https://darknetdiaries.com/episode/0/"
        url = url.replace("0", str(i))

        page = get(url)
        page_soup = BeautifulSoup(page.text, 'html.parser')

        scripts = page_soup.findAll('script')
        script = str(scripts[3])
        script = script.replace("<script>", "", 1)
        script = script.replace("window.playerConfiguration = ", "", 1)
        script = script.replace("</script>", "", 1)
        json_dict = json.loads(script)

        link = json_dict["episode"]["media"]["mp3"]

        title = json_dict["episode"]["title"]
        title = title.replace(":", "")

        json_ddd.update({str(i): {"title": title, "link": link}})

        print(str(i) + ". Added JSON entry: " + title)

    json_ddd_str = json.dumps(json_ddd, indent=4)

    with open("DDJ.json", 'w') as f:
        f.write(json_ddd_str)
    print("Exported to a file.")


def check_file():
    if exists("DDJ.json"):
        print("JSON file found, proceeding...")
        if getsize("DDJ.json") != 14660:
            print("Corrupted JSON file found, creating a brand new DDJ.json file...\n")
            create_json()
        else:
            print()
    else:
        print("JSON file not found, creating a brand new DDJ.json file...\n")
        create_json()
