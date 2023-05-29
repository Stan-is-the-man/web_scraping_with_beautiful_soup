from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text
# print(content)

soup = BeautifulSoup(content, 'lxml')

box = soup.find('article', class_='main-article')

# Get the movie title
title = box.find('h1').get_text()
print(title)

# Get the subtitles
# transcript = box.find('div', class_='full-script').get_text()
# Add (strip=True, separator=' ')  for exporting to txt files
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

# Export to a txt file:
with open(f'{title}.txt', 'w', encoding="utf-8") as file:
    file.write(transcript)
