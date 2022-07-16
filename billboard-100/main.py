from bs4 import BeautifulSoup
import requests


date = input("Which year do you want to see? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, 'html.parser')

song_names_title = soup.select(selector="li h3")
song_names = [song.getText().strip("\n\n\t\n\t\n\t\t\n\t\t\t\t\t") for song in song_names_title]
artist_names = soup.select(selector="li span")
artists = [artist.getText().strip("\n\n\t\n\t\n\t\t\n\t\t\t\t\t") for artist in artist_names]
print(song_names)
print(artists)