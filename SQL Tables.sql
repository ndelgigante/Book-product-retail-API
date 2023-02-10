CREATE DATABASE book;
CREATE TABLE users (
  userid INT PRIMARY KEY AUTO_INCREMENT,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(100) NOT NULL,
  userRole VARCHAR(100) NOT NULL
);

CREATE TABLE orders (
  orderNumber INT PRIMARY KEY AUTO_INCREMENT,
  orderDate DATE NOT NULL,
  userid INT,
  FOREIGN KEY (userid) REFERENCES users(userid)
);

CREATE TABLE product_reviews (
  review_id INT PRIMARY KEY AUTO_INCREMENT,
  product_id INT NOT NULL,
  user_id INT,
  rating INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(userid)
);

CREATE TABLE products (
  productid INT PRIMARY KEY AUTO_INCREMENT,
  productname VARCHAR(100) NOT NULL,
  productdescription TEXT NOT NULL,
  quantity INT NOT NULL,
  MSRP DECIMAL(10, 2) NOT NULL
);

