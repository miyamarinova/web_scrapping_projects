from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/newest")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article in articles:
    article_texts.append(article.getText())
    link = article.contents[0].get("href")
    article_links.append(link)


article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)



