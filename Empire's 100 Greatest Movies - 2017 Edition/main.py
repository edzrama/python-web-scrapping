from requests import get
from bs4 import BeautifulSoup

# Get 100 Greatest movies 2017 edition from Empire and list to new text file movies.txt
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = get(URL)
#
soup = BeautifulSoup(response.text, "html.parser")
titles = [title.getText() for title in soup.find_all("h3", class_="title")]
titles.reverse()
new_text = "".join(f"{title}\n" for title in titles)
with open("movies.txt","w",encoding="UTF-8") as file:
    file.write(new_text)


