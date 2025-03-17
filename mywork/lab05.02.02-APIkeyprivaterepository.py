import requests
import json
from config import apikeys as cfg

filename = "private.json"

url = 'https://api/github.com/repos/UWASIKLK/privateone.git'

#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
#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
#apikey = "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"
apikey = cfg["githubkey"]

#response = requests.get(url)
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)