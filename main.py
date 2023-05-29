from bs4 import BeautifulSoup
import requests

# website = 'https://subslikescript.com/movie/Titanic-120338'
root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text
# print(content)

soup = BeautifulSoup(content, 'lxml')

# SCRAPING JUST ONE LINK - fin()):
box = soup.find('article', class_='main-article')

# Get the movie title
title = box.find('h1').get_text()


# Get the subtitles - add (strip=True, separator=' ')  for exporting to txt files
# transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')  # get an element

# SCRAPING MULTIPLE LINKS WITH THE SAME PAGE findall():
all_transcripts = box.find_all('a', href=True)  # get a list of all the elements
links = []
for link in all_transcripts:
    links.append(link['href'])

for link in links:
    website = f'{root}/{link}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    # Export to a txt file:
    with open(f'{title}.txt', 'w', encoding="utf-8") as file:
        file.write(transcript)
