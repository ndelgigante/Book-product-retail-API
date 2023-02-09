import pandas as pd
from DatabaseManager import DatabaseManager 
import mysql.connector
from Models.products import Product

dm = DatabaseManager()

book2 = [{
    "Book Id": 0,
    "Book Name": "To Kill a Mockingbird",
    "Book Description": "The novel examines racism in the Americcan south trhough the innocent wide eyes of a clever young girl.",
    "Book Quantity": 50,
    "Book MSRP": 34.99
    }]



conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="book"
)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS book(
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    book_name VARCHAR(230) NOT NULL,
    book_description VARCHAR(230) NOT NULL,
    book_Quantity INT,
    book_MSRP FLOAT)"""
)


class products:
    def __init__(self):
        self.bookdf = dm.get_df("book")

    #book1 = [0, "'To kill Moackingbird'", "'something'", 50, 34.99]
    #dm.insert("book", book1)

    #cur.execute("""SELECT * FROM book """)

    # df = pd.DataFrame(book2)
    #print(df)

    def add_book(book1):
       

       dm.insert("book", book1)

       pass
        

    def remove_Booksid(self, bookid):
        dm.delete("book", f"book_id={bookid}")
        self.bookdf = dm.get_df("book")

    def search_Books(self, author):
        
        # cur.execute(f'SELECT * FROM book WHERE book_name={bookname}')
        # print("book")

    #test = input("please enter a book iD to remove a book")
    #remove_Booksid(test)

    test = input("please enter a book name you want to search")
    search_Books(test)