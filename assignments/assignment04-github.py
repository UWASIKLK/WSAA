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

#decode = contents = contents.decoded_content.decode("utf-8")

fileurl = contents.download_url
#print(fileurl)  #testing, this will print the url to the sample text file

response = requests.get(fileurl)
contentoffile = response.text
print(contentoffile, "\n") #printing original sample text with 'Andrew' name

#counting how many 'Andrew' is in the sample text
count = contentoffile.count("Andrew")
print(f"This sample text contains {count} instances of the name 'Andrew'. \n")

replacename = contentoffile.replace("Andrew", "Katarina")
print(replacename)

#defining the new txt file where the replaced text will be saved
newfilepath = "assignments/sampletextnew.txt"

githubresponse = repo.create_file(newfilepath,"Name 'Andrew' has bee updated to name 'Katarina' and text was saved in new file", replacename)
print("\n\nNew file with the updated text was created successfully:", githubresponse)

'''
#this is as per originall assignment request to update the existing file

githubresponse = repo.update_file(contents.path,"Name 'Andrew' has bee updated to name 'Katarina'",replacename,contents.sha)
print("Text file has been updated successfully:", githubresponse)'
'''