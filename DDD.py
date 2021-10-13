import requests
from bs4 import BeautifulSoup

start = int(input("Start downloading from Episode: "))
end = int(input("End downloading from Episode (including this number): "))
   
for i in range(start, end+1):
    url = "https://darknetdiaries.com/episode/0/"
    url = url.replace("0", str(i))
    
    page = requests.get(url)
    page_soup = BeautifulSoup(page.text, 'html.parser')

    scripts = page_soup.findAll('script')
    script = str(scripts)

    index_start_link = script.find('"mp3": "')
    index_end_link = script.find('"', index_start_link + len('"mp3": "'))
    link =  script[index_start_link + len('"mp3": "'): index_end_link ]

    h1s = str(page_soup.findAll('h1'))
    index_start_h1 = h1s.find('EP')
    index_end_h1 = h1s.find('</h1>')
    ext = '.mp3'
    
    file_name = h1s[index_start_h1 : index_end_h1] + ext
    file_name = file_name.replace(":", "")
    
    print(''.join( ( str(i),". ", file_name, ": ", link ) ) )
    
    podcast = requests.get(link) 
    
    with open(file_name , 'wb') as local_file:
        local_file.write(podcast.content)


