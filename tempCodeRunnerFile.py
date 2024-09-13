@app.route("/books/<int:bid>",method=['DELETE'])
# def delete_book(bid):
#     if bid in books_dict:
#         del books_dict[bid]
#         return {"data" : "Removal Successful"}
#     return {"error" : "Nothing is removed"}