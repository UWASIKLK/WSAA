# program which will get the dataset of 'exchequer account (historical series) from the CSO, and store it into a file called 'cso.json' in data folder.

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

response = response = requests.get(url)
##print(response.json())

if response.status_code != 200:
     print("There is an error: " + str(response.status.code))
else: 
    with open ("data/cso.jason", "wt") as fp:
      json.dump(response.json(), fp)
    print("Data succesfully wrtitten to the file cso.json")
