"""

# Author: Sichun Yin
# Last update: 29/07/2018
# For the requirements, installation and usage, please find further
# details in README.md section A2

"""

import requests
import datetime
import sqlite3
import sys

if len(sys.argv) > 1:
    sqlite_file = sys.argv[1]
else:
    sqlite_file = "daily_stock.sqlite"  # name your database.
table_name = sqlite_file[ :sqlite_file.find(".")]
url = "https://www.alphavantage.co/query"  # url of Alpha Vantage.
symbols = {"Apple": "AAPL","Alphabet": "GOOG","Amazon": "AMZN"}  # list companies of your choice and their symbols.
arg_dict = {"apikey": "8K64WVV2CXLH0KF8","function": "TIME_SERIES_DAILY","outputsize": "full"}
# specify your query here
headsDict = {"Content-Type": "application/json"}  # http request header

options = "?"
for key in arg_dict.keys():
    options += key + "=" + arg_dict[key] + "&"

url += options
base_url = url  # just a copy of the base of url.
ten_years_before = datetime.datetime.now().year - 10  # specify the number of the year ten years ago...

print("Victor: creating the database and making the connection...")
try:
    conn = sqlite3.connect(sqlite_file)  # create a database and/or make a connection to it.
    c = conn.cursor()

    c.execute("CREATE TABLE {tn} (date text, stock text, open real, high real, low real, close_value real, \
    volume integer)".format(tn=table_name))  # create a table.
except Exception as e:
    print("Victor: failed to create a table")
    print(e)
    sys.exit(1)
else:
    print("Victor: created a table in the database...")

for i in symbols.keys():
    url += "&symbol=" + symbols[i]
    try:
        response = requests.get(url,headers=headsDict)
        results = response.json()["Time Series (Daily)"]
        print("Victor: received stock data from", i)
        print("Victor: processing the data...")
        for key in results.keys():
            if int(key[:4]) >= ten_years_before:  # we only need the data recorded in the most recent ten years.
                result = results[key]
                c.execute(
                    "INSERT INTO " + table_name + " VALUES ({date}, {stock}, {open}, {high}, {low}, {close}, \
                    {volume})".format(date="'" + key + "'",stock="'" + symbols[i] + "'",open=result["1. open"]\
                    ,high=result["2. high"],low=result["3. low"],close=result["4. close"],volume=result["5. volume"]))
            else:
                break  # only use break if you can make sure the data received is in descending order by years;
                # otherwise, use continue instead.
    except requests.RequestException as e:
        print("Victor: request has not been successful! Check this out: ")
        print(e)
    except Exception as h:
        print("Victor: something goes wrong! Check this out: ")
        print(h)

print("Victor: Check your database out in the current directory!")
conn.commit()
conn.close()
