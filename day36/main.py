import requests
from datetime import date, timedelta
from twilio.rest import Client

import config

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

now = date.today()
yesterday = now - timedelta(days=1)
the_day_before_yesterday = now - timedelta(days=2)


def percentage_difference(a, b):
    return (abs(a - b) / ((a + b) / 2)) * 100


def stock_monitor():
    alpha_vantage_url = "https://www.alphavantage.co/query"
    av_parametres = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": config.ALPHA_VINTAGE_API_KEY,
    }

    alphavantage_response = requests.get(alpha_vantage_url, params=av_parametres)
    alphavantage_response.raise_for_status()
    av_data = alphavantage_response.json()["Time Series (Daily)"]
    av_data_day_before_yesterday = av_data[str(the_day_before_yesterday)]
    avg_stock_value_day_before_yesterday = (
        float(av_data_day_before_yesterday["1. open"])
        + float(av_data_day_before_yesterday["2. high"])
        + float(av_data_day_before_yesterday["3. low"])
        + float(av_data_day_before_yesterday["4. close"])
    ) / 4

    av_data_yesterday = av_data[str(yesterday)]
    avg_stock_value_yesterday = (
        float(av_data_yesterday["1. open"])
        + float(av_data_yesterday["2. high"])
        + float(av_data_yesterday["3. low"])
        + float(av_data_yesterday["4. close"])
    ) / 4
    diff = percentage_difference(
        avg_stock_value_day_before_yesterday, avg_stock_value_yesterday
    )
    if avg_stock_value_yesterday > avg_stock_value_day_before_yesterday:
        return round(diff, 4)
    else:
        return round(diff, 4) * -1


def get_news():
    news_api_url = "https://eventregistry.org/api/v1/article/getArticles"
    news_parametres = {
        "keyword": COMPANY_NAME,
        "from": str(now),
        "resultType": "articles",
        "articlesCount": 3,
        "articlesSortBy": "sourceImportance",
        "apiKey": config.NEWS_API,
    }
    news_response = requests.get(news_api_url, params=news_parametres)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]["results"]
    news_report = []
    for news in news_data:
        news_report.append(f"{news['title']}: {news['url']}")
    return news_report


tesla_stock_change = stock_monitor()
print(tesla_stock_change)
if tesla_stock_change > 1.5:
    tesla_news_report = get_news()
    client = Client(config.TWILIO_SID, config.AUTH_KEY)
    message = client.messages.create(
        body=f"""TSLA: 🔺{tesla_stock_change}%
        {tesla_news_report[0]},
        {tesla_news_report[1]},
        {tesla_news_report[2]}""",
        from_="whatsapp:+14155238886",
        to="whatsapp:+48531464555",
    )
    print("sent")
elif tesla_stock_change < -1.5:
    tesla_news_report = get_news()
    client = Client(config.TWILIO_SID, config.AUTH_KEY)
    message = client.messages.create(
        body=f"""TSLA: 🔻{tesla_stock_change}%
        {tesla_news_report[0]},
        {tesla_news_report[1]},
        {tesla_news_report[2]}""",
        from_="whatsapp:+14155238886",
        to="whatsapp:+48531464555",
    )
