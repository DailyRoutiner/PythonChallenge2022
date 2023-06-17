import requests
import json
import os
from twilio.rest import Client

STOCK_NAME = "TLSA"
COMPANY_NAME = "Tesla Inc"

VIRTUAL_TWILIO_NUMBER = ""
VERIFIED_NUMBER = ""



# with open("./test_data.json", "r") as file:
#     json_data = json.load(file)         # set json format
#     json_data = json_data["Time Series (Daily)"]
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

data = requests.get(STOCK_ENDPOINT, params=stock_params)
data.raise_for_status()
stock_data = data.json()["Time Series (Daily)"]


# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
list = [value["4. close"] for (key, value) in stock_data.items()]

# Get the day before yesterday's closing stock price
yesterday_stock = float(list[0])
day_before_yesterday_stock = float(list[1])

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
up_down = None
diff = yesterday_stock - day_before_yesterday_stock
if diff > 0:
    up_down = "+"
else:
    up_down = "-"
#average = (yesterday_stock + day_before_yesterday_stock) / 2
# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
#percentage = diff / average * 100
diff_percent = round((diff / yesterday_stock) * 100, 2)
print(diff_percent)

# If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 5:
    # Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    # Ex) GET https://newsapi.org/v2/everything?q=tesla&from=2023-02-21&sortBy=publishedAt&apiKey=
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apikey": NEWS_API_KEY
    }

    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    # Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    articles = response.json()['articles'][:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#Create a new list of the first 3 article's headline and description using list comprehension.
    new_list = [f"Headline: {article['title']}.\n Brief: {article['description']}" for article in articles]

# Send each article as a separate message via Twilio.
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure

    for news in new_list:
        message = client.messages \
                        .create(
                             body=f"{COMPANY_NAME}: {up_down}{diff_percent}% \n"
                                  f"{news}",
                             from_="+15076688948",
                             to="+821034812939"
                         )
    #print(message.sid)


#Optional : Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

