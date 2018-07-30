# QuantifulTest
A report contains specifications of three questions
## Requirements
* [requests](http://docs.python-requests.org/en/master/)
* datetime/sqlite3 (These two modules are already included in Python library)
* Bash Shell
## Installations
* Clone the repo:
```
git clone https://github.com/VictorSichun/QuantifulTest
```
## A1
### Introduction
A1.py is a consumer of a web service provider [National Oceanic and Atmospheric Administration](https://www.ncdc.noaa.gov/cdo-web/webservices/v2#gettingStarted),
which enables users to get access to the climate data. The code inside of A1.py basically calculates the average precipitation
of state of Florida, in the USA, at 2:00 pm, on 24 Aug 2000.
### Usage
* Enter into QuantifulTest
```
cd QuantifulTest
```
* Run on Terminal
```
Python3 A1.py
```

## A2
### Introduction
A2.py is not only a consumer of [AlphaVantage API](https://www.alphavantage.co/) but also a database creater. It helps 
users to get access to, retrieve and store the stock data. The code inside of A2.py collects Apple, Alphabet and Amazon daily stock data for the last 10 years 
and store this in a SQLite database.
### Usage
* Enter into QuantifulTest:
```
cd QuantifulTest
```
* Run on Terminal:
```
Python3 A1.py arg
```
Replace ```arg``` by the name of the database you want; otherwise, the database will be named ```daily_stock.sqlite``` by default.

## A3
### Introduction
A3 is a bash file exports the data inside a specified database into a .csv file.
### Usage
* Enter into QuantifulTest:
```
cd QuantifulTest
```
* Run on Terminal:
```
./A3 arg
```
Replace ```arg``` by the name of an existing database; otherwise, it would run into an error
## Report

Sorry for the hard-coding:sweat_smile:, I was trying to focus on the implementations of the specific tasks and left other potential users, because functionality is the most important part in my future job. 
The reason why I code with Python is that:
1. Python is easy and I'm familiar with Python;
2. Python is handy for the data mining purposes and it is suitable for these particular tasks.

The thoughts for A1 and A2 are pretty simple: 
1. Read through the API library and make sure I understood the relationship of the database;
2. Setup all the required parts of the query at the beginning(A set of prompt commands can be inserted here in the future);
3. Make sure the required information is managable and extendable;
4. Send the constructed http request safely(use try...except block to ensure the security of the code);
5. 'Victor' helps users to keep track of the progress.

For A3:
1. Used roughly one hour to learn how to program with bash;
2. Played around with it;
3. No matter if I could be selected, I had fun and learnt a lot. Many thanks!

