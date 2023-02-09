import pandas as pd
from DatabaseManager import DatabaseManager 
import mysql.connector

class Books:
    def __init__(self, bookid, bookname, bookdesc, quantity, msrp):
        self.bookid = bookid
        self.bookname = bookname
        self.bookdesc = bookdesc
        self.quantity = quantity
        self.msrp = msrp

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

    def add_book(self, Books):
        

    def remove_Booksid(self, bookid):
        dm.delete("book", f"book_id={bookid}")

    def search_Books(self, bookname):
        
        # cur.execute(f'SELECT * FROM book WHERE book_name={bookname}')
        # print("book")

    #test = input("please enter a book iD to remove a book")
    #remove_Booksid(test)

    test = input("please enter a book name you want to search")
    search_Books(test)