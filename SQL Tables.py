import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="book"
)
cur = conn.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS book")

cur.execute("""CREATE TABLE IF NOT EXISTS users (
  userid INT PRIMARY KEY AUTO_INCREMENT,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(100) NOT NULL,
  userRole VARCHAR(100) NOT NULL
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS orders (
  orderNumber INT PRIMARY KEY AUTO_INCREMENT,
  orderDate DATE NOT NULL,
  userid INT,
  FOREIGN KEY (userid) REFERENCES users(userid)
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS product_reviews (
  review_id INT PRIMARY KEY AUTO_INCREMENT,
  product_id INT NOT NULL,
  user_id INT,
  rating INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(userid)
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS product(
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    book_name VARCHAR(230) NOT NULL,
    book_description VARCHAR(230) NOT NULL,
    book_author VARCHAR(230),
    book_genre VARCHAR(30),
    book_Quantity INT,
    book_MSRP FLOAT)"""
)

