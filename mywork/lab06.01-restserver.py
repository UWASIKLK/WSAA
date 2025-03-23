from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='',static_folder='staticpages')

@app.route('/')
def index():
    return "Hello and Welcome"

@app.route('/books', methods =['GET'])
def getall():
    return "Get all books"

@app.route('/books/<int:id>', methods = ['GET'])
def bookbyid(id):
    return f"Book find by ID: {id}"

@app.route('/books', methods=['POST'])
def createbook():
    jsonstring = request.json
    return f"New book added with details: {jsonstring}"

@app.route('/books/<int:id>', methods=['PUT'])
def updatebook(id):
    jsonstring = request.json
    return f"Book with ID:{id} is updated with: {jsonstring}"

@app.route('/books/<int:id>', methods =['DELETE'])
def deletebook(id):
    return f"Book with ID:{id} is now deleted."

if __name__ == "__main__":
    app.run(debug = True)