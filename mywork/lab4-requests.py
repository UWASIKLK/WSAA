# writing a module to interact with the API created at http://andrewbeatty1.pythonanywhere.com/books 

import requests

#testing if request works on google website
url = "http://google.com"
response = requests.get(url)
print(response.text)


#write a code to get books from http://andrewbeatty1.pythonanywhere.com/books
URL = "http://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(URL)
print(response.json())


#convert into a function and call it from insade a if __name__ == "__main__":
def readbooks():
    response = requests.get(URL)
    #we could do checking for correct response code here
    return response.json()
if __name__ == "__main__":
    print(readbooks())
