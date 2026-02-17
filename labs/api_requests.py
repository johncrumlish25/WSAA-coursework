# api_requests.py
# This program will iteract with an API
# Author: John Crumlish

import requests 
URL = "http://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(URL) 
print (response.json()) 


def readbooks():
    response = requests.get(URL)  
    return response.json()
if __name__ == "__main__": 
    print (readbooks())


def readbook(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
    return response.json()



def createbook(book):
    response = requests.post(URL, json=book)
    return response.json()


def updatebook(id, book):
    puturl = URL + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()



def deletebook(id): 
    deleteurl = URL + "/" + str(id) 
    response = requests.delete(deleteurl) 
    return response.json() 