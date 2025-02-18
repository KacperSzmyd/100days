from NewsHeaders import NewsHeader
from bs4 import BeautifulSoup
import requests
import random

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
response.raise_for_status()

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
headers = soup.select(selector=".titleline a.storylink")
scores = soup.select(selector="span.score")
nhs = []
for news in range(len(headers)):
    title = headers[news].text
    link = headers[news].get("href")
    score = int(scores[news].text.split()[0])
    nh = NewsHeader(title, link, score)
    nhs.append(nh)


def quickselect_max(arr, k):
    pivot = random.choice(arr).score
    lows = [x for x in arr if x.score < pivot]
    highs = [x for x in arr if x.score > pivot]
    pivots = [x for x in arr if x.score == pivot]

    if len(highs) == 0:
        return pivots[0]
    elif len(highs) == 1:
        return highs[0]
    else:
        return quickselect_max(highs, k - len(lows) - len(pivots))


print([x.score for x in nhs])
print(quickselect_max(nhs, len(nhs)))
