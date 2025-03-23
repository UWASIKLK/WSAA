import requests
import json
import urllib.parse
from config import apikeys as cfg

#url = 'https://en.wikipedia.org'
url = "https://en.wikipedia.org/wiki/Pat_%26_Mat"

apiKey = cfg["htmltopdfkey"]

apiurl = "https://api.html2pdf.app/v1/generate"

params = {"url": url, "apiKey": apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiurl + "?" +  parsedparams

response = requests.get(requestUrl)
print(response.status_code)  #to make sure that we will get status 200

results = response.content

with  open("document.pdf", 'wb') as handler:
     handler.write(results)





