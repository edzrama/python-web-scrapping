from bs4 import BeautifulSoup
# import lxml

# get values from html file
with open("website.html",encoding="utf8") as website:
    contents = website.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title.string)
print(soup.prettify())

all_anchors = soup.find_all(name="a")

for tag in all_anchors:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(id="name").getText()

print(heading)

section_heading = soup.find(name="h3", class_="heading").getText()
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)


