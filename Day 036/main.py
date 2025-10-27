import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
PERCENTAGE_THRESHOLD = 5  #If you want to make the alerts looser, lower this.

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH")
client = Client(account_sid, auth_token)


stock_api = os.getenv("STOCK_API")
news_api = os.getenv("NEWS_API")

twilio_whatsapp_receiver = os.getenv("TWILIO_WHATSAPP_RECEIVER")
twilio_whatsapp_number = os.getenv("TWILIO_WHATSAPP_NUMBER")

if not all([account_sid, auth_token, stock_api, news_api]):
    raise EnvironmentError("Missing environment variables. Check your .env file.")

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api,
}

stock_r = requests.get(STOCK_ENDPOINT,params=parameters)
stock_data = stock_r.json().get("Time Series (Daily)")
if not stock_data:
    raise Exception("Error: Could not fetch stock data. Check your API key or rate limit.")

#Yesterday's closing price
data_list = [value for (key, value) in stock_data.items()]
yesterdays_data = data_list[0]
yesterdays_closing_price = float(yesterdays_data["4. close"])

#Day before closing price
day_before_data = data_list[1]
day_before_closing_price = float(day_before_data["4. close"])

#Price diff calculations
price_diff = abs(yesterdays_closing_price-day_before_closing_price)
pct_diff = ((yesterdays_closing_price - day_before_closing_price) / day_before_closing_price) * 100
pct_diff_pos = abs(pct_diff)

direction = "🔺" if pct_diff > 0 else "🔻"

#If percentage is bigger than our threshold, then we request the news from api and send them to the number.
if pct_diff_pos >PERCENTAGE_THRESHOLD:
    print("Get News")
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": news_api,
        "sortBy": "publishedAt",
        "language": "en",
    }
    news_r = requests.get(NEWS_ENDPOINT, params=news_params)
    articles_list = news_r.json()["articles"][:3]
    for article in articles_list:
        message = client.messages.create(
        from_=f"whatsapp:{twilio_whatsapp_number}",
        to=f"whatsapp:{twilio_whatsapp_receiver}",
        body = (
        f"{STOCK_NAME}: {direction}{pct_diff:.2f}%\n\n"
        f"Headline: {article['title']}\n\n"
        f"Brief: {article['description']}"
        ))
        print(message.sid)