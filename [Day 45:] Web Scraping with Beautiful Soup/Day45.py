import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

article_texts = []
article_links = []

articles = soup.find_all("span", class_="titleline")

for article in articles:
    link_tag = article.find("a")
    article_texts.append(link_tag.getText())
    article_links.append(link_tag.get("href"))

article_upvotes = [
    int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")
]

#print(article_texts)
#print(article_links)
#print(article_upvotes)


largest_number_of_upvotes = max(article_upvotes)
largets_index = article_upvotes.index(largest_number_of_upvotes)

print(article_texts[largets_index])
print(article_links[largets_index])