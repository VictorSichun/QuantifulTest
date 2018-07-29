"""

# Author: Sichun Yin
# Last update: 29/07/2018
# For the requirements, installation and usage, please find further
# details in README.md section A1

"""
import requests

url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data"  # the url of api we gonna consume
myToken = "OXaMoiAsYbqmucQfIMgnTFFKGzXJhhFB"    # token for Victor
headsDict = {"token": "{}".format(myToken), "Content-Type":"application/json"}   # http request header, add whatever you need
data_info = {"locationid": "FIPS:12", "datasetid": "PRECIP_HLY", "startdate": "2000-08-24T14:00:00", "enddate": "2000-08-24T14:00:00"}
#   you have to specify a bunch of information before sendin th request
options = "?"
for key in data_info.keys():
    options += key + "=" + data_info[key] + "&"

url += options

try:
    response = requests.get(url, headers=headsDict)
except requests.RequestException as e:
    print("Victor: Bad luck! Something went wrong while requesting to the server, check this out: ")
    print(e)
except Exception as h:
    print("Victor: Whoops! Check this out: ")
    print(h)
else:
    print("Victor: Congrats! We've got some data from server...")
    results = response.json()["results"]
    amount_of_precipitation = 0
    for i in results:
        amount_of_precipitation += i["value"]
    average_precipitation = amount_of_precipitation/len(results)
    print("Victor: The result is", average_precipitation)
finally:
    print("Thanks for using!!!")

