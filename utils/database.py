"""
Concerned with storing and retrieving books from a csv file.
Format of the csv file:

name,author,read\n
name,author,read\n
name,author,read\n
"""


books_file = "books.txt"



def add_book(name, author):
    with open(books_file, "a") as file:
        file.write(f"{name},{author},0\n")



def get_all_books():
    return books



def mark_book_as_read(name):
    for book in books:
        if book["name"] == name:
            book["read"] = True



def delete_books(name):
    global books
    books = [book for book in books if book["name"] != name]

