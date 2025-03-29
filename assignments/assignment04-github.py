# assignment 4

#pip install PyGithub
from github import Github
import requests
from config import config as cfg


apikey = cfg["githubkey"]

ginstance = Github(apikey)

repo = ginstance.get_repo("UWASIKLK/WSAA")
print(repo.clone_url)

contents = repo.get_contents("assignments/sampletext.txt")

decode = contents.decoded_content.decode("utf-8")

filerul = decode.download_url
print(filerul)

response = requests.get(filerul)
contentoffile = response.text
print(contentoffile)

count = 0
for name in contentoffile.split():
    if name == "Andrew":
        count += 1
print(f"This sample text contains {count} instances of the name 'Andrew'")

replacename = contentoffile.replace("Andrew", "Katarina")
print(replacename)

githubresponse = repo.update_file(contents.path,"Name 'Andrew' has bee updated to name 'Katarina'",replacename,contents.sha)
print("Text file has been updated successfully:", githubresponse)