import csv

def read_books(file_name):
    books = []
    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            book = {
                'Title': row['Title'],
                'Author': row['Author'],
                'ISBN': row['ISBN'],
                'Price': float(row['Price']) # convert price to float
            }
            books.append(book)
    return books
def search_by_author(author, books):
    books_by_author = []
    for book in books:
        if author(book) == author:
            books_by_author.append(book)
    return books_by_author

def search_by_title(title, books):
    books_by_title = []
    for book in books:
        if title(book) == title:
            books_by_title.append(book)
    return books_by_title

def search_by_isbn(ISBN, books):
    books_by_isbn = []
    for book in books:
        if isbn(book) == isbn:
            title = book.title
            price = book.price
            books_by_isbn.append((title, price))
    return books_by_isbn

def search_by_price(price, books):
    books_by_price=[]
    for book in books:
        max_price=float(input("Maximum price is "))
        min_price=float(input("Minimum price is "))
    if min_price <= book.price <= max_price:
            books_by_price.append(book)
    return books_by_price
    
search_method=['Search by author','Search by ISBN','Search by price']
search_choice=input('How do you want to search? ')

if search_choice == search_method[0]:
    author_name = input("Enter the author's name: ")
    result = search_by_author(author_name, books)
    print(result, "are/is the book(s) from this author")
    
    
elif search_choice == search_method[1]:
    book_isbn = input("Enter the book's ISBN: ")
    result = search_by_isbn(book_isbn, books)
    print(result, "are/is the book(s) with this isbn")
    
elif search_choice == search_method[2]:
    price_range= input("Enter the price range ")
    result = search_by_price(price_range, books)
    print(result, "are/is the book(s) within this price range")
    
else:
    print("Try again")
    