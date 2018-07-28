import requests

url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data"
myToken = "OXaMoiAsYbqmucQfIMgnTFFKGzXJhhFB"
headsDict = {"token": "{}".format(myToken), "Content-Type":"application/json"}
data_info = {"locationid": "FIPS:12", "datasetid": "PRECIP_HLY", "date": "2000-08-24T14:00:00"}
options = "?datasetid=" + data_info["datasetid"] + "&locationid=" + data_info["locationid"] + \
          "&startdate=" + data_info["date"] + "&enddate=" + data_info["date"] + "&sortorder=DESC"
url += options

try:
    response = requests.get(url, headers=headsDict)
    print(response.json())
except requests.RequestException as e:
    print(e)

else:
    results = response.json()["results"]
    amount_of_precipitation = 0
    print(results)
    for i in results:
        amount_of_precipitation += i["value"]
    average_precipitation = amount_of_precipitation/len(results)
    print(average_precipitation)

