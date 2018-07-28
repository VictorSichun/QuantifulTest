import requests
import datetime
import sqlite3

sqlite_file = "daily_stock.sqlite"
url = "https://www.alphavantage.co/query?"
symbols = {"Apple": "AAPL","Alphabet": "GOOG","Amazon": "AMZN"}
arg_dict = {"apikey": "8K64WVV2CXLH0KF8","function": "TIME_SERIES_DAILY","outputsize": "full"}
headsDict = {"Content-Type": "application/json"}

url += "apikey=" + arg_dict["apikey"] + "&function=" + arg_dict["function"] + "&outputsize=" + arg_dict["outputsize"]

ten_year_before = datetime.datetime.now().year - 10

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute("CREATE TABLE {tn} (date text, stock text, open real, high real, \
        low real, close_value real, volume integer)".format(tn="Daily_Stock"))

for i in symbols.keys():
    url += "&symbol=" + symbols[i]
    try:
        response = requests.get(url,headers=headsDict)
        results = response.json()["Time Series (Daily)"]

        for key in results.keys():
            if int(key[:4]) >= ten_year_before:
                result = results[key]
                c.execute(
                    "INSERT INTO Daily_Stock VALUES ({date}, {stock}, {open}, {high}, {low}, {close}, {volume})".format(
                        date=key, stock= "'"+symbols[i]+"'", open=result["1. open"], high=result["2. high"], low=result["3. low"]
                        , close=result["4. close"], volume=result["5. volume"]))
    except requests.RequestException as e:
        print(e)
    except Exception as h:
        print(h)
conn.commit()
conn.close()