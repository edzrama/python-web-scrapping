from bs4 import BeautifulSoup
from requests import get

response = get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.title)


# Get first entry
# title = soup.find(name="a", class_="titlelink").getText()
# link = soup.find(name="a", class_="titlelink").get("href")
# score = soup.find(name="span", class_="score").getText()
# print(title)
# print(link)
# print(score)


article_titles = []
article_links = []
article_scores = []
# get all the articles in current page
articles = (soup.find_all(name="a", class_="titlelink"))
for article in articles:
    article_titles.append(article.getText())
    article_links.append(article.get("href"))
# article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# get all article scores
rows = soup.find_all(name="td", class_="subtext")
for row in rows:
    score = row.find(name="span", class_="score")
    # append 0 when article got no points
    if score is None:
        article_scores.append(0)
    else:
        article_scores.append(int(score.string.split()[0]))


max_value = max(article_scores)
max_index = article_scores.index(max_value)
# Print top article including the link and points
print(f'top article: {article_titles[max_index]}')
print(f'Link: {article_links[max_index]}')
print(f'Points: {article_scores[max_index]}')


