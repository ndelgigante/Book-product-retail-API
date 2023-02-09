import pandas as pd
import DatabaseManager 
import mysql.connector

class Books:
    def __init__(self, bookid, bookname, bookdesc, quantity, msrp):
        self.bookid = bookid
        self.bookname = bookname
        self.bookdesc = bookdesc
        self.quantity = quantity
        self.msrp = msrp


book = [{
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



df = pd.DataFrame(book)
print(df)

def add_Books():
    DatabaseManager.insert()
    

def remove_Books():
    DatabaseManager.delete()
    pass

def search_Books(self, table_name, bookname):
    self.cur.execute(f'SELECT * FROM {table_name} WHERE {bookname};')
    self.conn.commit()
    