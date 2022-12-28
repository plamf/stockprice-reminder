import json
import smtplib
import requests
from decimal import Decimal

# Read Config File
config = ""
with open(r"config.json", "r", encoding="utf-8") as fs:
    config = json.load(fs)

# Read Portfolio File
portfolio = ""
with open(r"portfolio.json", "r", encoding="utf-8") as fs:
    portfolio = json.load(fs)

for stock in portfolio:
    #Check Prices
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock['Symbol']}&interval=60min&apikey={config['apiKey']}"
    r = requests.get(url)
    resultJson = r.json()

    latestTimestamp = list(resultJson['Time Series (60min)'].items())[0]
    latestPrice = Decimal(latestTimestamp[1]['4. close'])

    targetPrice = Decimal(stock['Price'])
    if latestPrice >= targetPrice:
        # Send Email
        message = f"""From: Stockprice Reminder <{config['mailSender']}>
To: Info Subscriber <{config['mailRecipient']}>
Subject: Reminder for {stock['Name']}

The Stock for {stock['Name']} has hit your target of {stock['Price']} and is currently at {latestPrice}.
"""
        with smtplib.SMTP(config['smtpServer'], config['smtpPort']) as mailServer:
            mailServer.login(config['mailSender'], config['mailSenderPassword'])
            mailServer.sendmail(config['mailSender'], [config['mailRecipient']], message)
