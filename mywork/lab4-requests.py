# writing a module to interact with the API created at http://andrewbeatty1.pythonanywhere.com/books 

import requests
'''
#testing if request works on google website
url = "http://google.com"
response = requests.get(url)
print(response.text)
'''

#write a code to get books from http://andrewbeatty1.pythonanywhere.com/books
URL = "http://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(URL)
#print(response.json())


#convert into a function and call it from insade a if __name__ == "__main__":
def readbooks():
    response = requests.get(URL)
    #we could do checking for correct response code here
    return response.json()
#if __name__ == "__main__":
    #print(readbooks())


#write a function for finding by id and test it
def readbook(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
    # we can do checking for correct response code here
    return response.json()
print(f"Reading a book by ID: ",readbook(562))


#write a conde to create and test
def createbook(book):
    book = {
        'author': "Claire Page",
        'title': "Good Night",
        'price': "32"
    }
    response = requests.post(URL, json=book)
    #we should check if we have correct status code
    return response.json()
print(f"New book addedd: ", createbook({}))


#write an update function
def updatebook(id, book):
    puturl = URL + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

#fetching the particular book
response = requests.get(f"{URL}/{1594}")
book = response.json()
if book.get('price') == 32: #changing the price
    book['price'] = 45
print(f"Changing a price on the book: ", updatebook(1594, book))



#write a delete function
def deletebook(id):
    deleteurl = URL + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

print(f"Deleting a book with ID = 1594: ",readbook(1594))

