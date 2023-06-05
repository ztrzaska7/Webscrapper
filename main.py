import requests
import os
from bs4 import BeautifulSoup
def web_scraper(url, filename):
    response=requests.get(url)
    if response.status_code==200:
        soup=BeautifulSoup(response.content, 'html.parser')

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
        print("Data saved ", filename)

    else:
        print("Downloading failed")

    url='https://www.matemundo.pl/?gclid=Cj0KCQjwj_ajBhCqARIsAA37s0ykTdsS-9p6zNgvPnmfC0u_6syNlbz8He5NQ9IpZ7Z78rWi0Tuaa7oaAiVPEALw_wcB'
    filename='output.html'
    web_scraper(url,filename)

current_directory=os.getcwd()
print(current_directory)
file_path=os.path.join(current_directory,filename)