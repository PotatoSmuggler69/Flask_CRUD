from flask import Flask, jsonify, render_template, request
from books import books,books_dict

app = Flask(__name__)

# Home Page of the APP
@app.route("/")
def index():
    return render_template("home.html")

# Gets all the books
@app.route('/books', methods=['GET'])
def get_books():
    return books_dict

#Get a specific book
@app.route("/books/<int:bid>", methods=['GET'])
def get_abook(bid):
    if bid in books_dict:
        return books_dict[bid]
    return {"Error" : "Book Not Found"}


#Delete a particular book
@app.route("/books/<int:bid>",methods=['DELETE'])
def delete_book(bid):
    if bid in books_dict:
        print(books_dict[bid])
        del books_dict[bid]
        return {"data" : "Removal Successful"}
    return {"error" : "Nothing is removed"}


# Post/create a book
@app.route("/books",methods=['POST'])
def add_book():
    temp_len = len(books_dict)+1
    books_dict[temp_len] = {
        "title":request.json['title'],
        "author":request.json['author'],
        "price":request.json['price'],
        "pages":request.json['pages'],
        "is_bestseller":request.json['is_bestseller']
    }
    return books_dict[temp_len]

# PUT/update a particular book
@app.route("/books/<int:bid>",methods=['PUT'])
def modify_book(bid):
    if bid in books_dict:
        books_dict[bid] = {
            "title":request.json['title'],
            "author":request.json['author'],
            "price":request.json['price'],
            "pages":request.json['pages'],
            "is_bestseller":request.json['is_bestseller']
        }
        return books_dict[bid]
    return {"error": f"Book does not exist with {bid}"}


if __name__ == '__main__':
    app.run(debug=True)