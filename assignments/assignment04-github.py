# assignment 4
# author: Katarina Siklodyova

#the package PyGithub needs to be installedto be able to use this program: pip install PyGithub
from github import Github
import requests
from config import config as cfg

#using the fine gained token generated in the Github and saved in config.py file which is in the .gitignore to prevent the key showing on Github
apikey = cfg["githubkey"]

ginstance = Github(apikey)

#getting the repository
repo = ginstance.get_repo("UWASIKLK/WSAA")
#print(repo.clone_url)  # this is testing, it will print my repository path

# get the contents of the sample text file
contents = repo.get_contents("assignments/sampletextoriginal.txt")
print(contents) # this will print out original sample text

#decode = contents = contents.decoded_content.decode("utf-8")

fileurl = contents.download_url
#print(fileurl) 

response = requests.get(fileurl)
contentoffile = response.text
print(contentoffile)

'''
count = 0
for name in contentoffile.split():
    if name == "Andrew":
        count += 1
print(f"This sample text contains {count} instances of the name 'Andrew'")

replacename = contentoffile.replace("Andrew", "Katarina")
print(replacename)

githubresponse = repo.update_file(contents.path,"Name 'Andrew' has bee updated to name 'Katarina'",replacename,contents.sha)
print("Text file has been updated successfully:", githubresponse)'
'''