from requests import get
from bs4 import BeautifulSoup
from json import loads

start = int(input("Start downloading from Episode: "))
end = int(input("End downloading from Episode (including this number): "))

for i in range(start, end + 1, 1):
    url = "https://darknetdiaries.com/episode/0/"
    url = url.replace("0", str(i))

    page = get(url)
    page_soup = BeautifulSoup(page.text, 'html.parser')

    scripts = page_soup.findAll('script')
    script = str(scripts[3])
    script = script.replace("<script>", "", 1)
    script = script.replace("window.playerConfiguration = ", "", 1)
    script = script.replace("</script>", "", 1)
    json_dict = loads(script)

    link = json_dict["episode"]["media"]["mp3"]

    title = json_dict["episode"]["title"]
    title = title.replace(":", "")

    print(str(i) + ". " + title + ": " + link)

    podcast = get(link)
    download = True

    if download:
        with open(title + ".mp3", 'wb') as local_file:
            local_file.write(podcast.content)
