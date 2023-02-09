import pandas as pd
import mysql.connector

class DatabaseManager:
    def __init__(self):
        #requires editing of the password and user to connection to actually access the database
        self.conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Book"
        )
        self.cur = self.conn.cursor()

    #param: 
    #table_name is a string identifier for the sql table
    def get_df(self,table_name):
        self.cur.execute(f'SELECT * FROM {table_name};')
        table_rows = self.cur.fetchall()
        df = pd.DataFrame(table_rows)
        return df

    #param: 
    #table_name is a string identifier for the sql table
    #values: is a list of the attribute values
    def insert(self,table_name, values):
        entry =" "
        for x in values:
            entry += ', '+ str(x)
        entry = entry[2:]
        self.cur.execute(f'INSERT INTO {table_name} VALUES({values});')
        self.conn.commit()
    
    #param:
    #table_name: is a string identifier for the sql table
    #condition: sql string condition for deletions (ie price < 3)
    def delete(self,table_name,condition):
        self.cur.execute(f'DELETE FROM {table_name} WHERE {condition};')
        self.conn.commit()


    #param:
    #table_name is a string identifier for the sql table
    #command: is a sql string with the SET and WHERE clause of the update syntax (ie SET column1 = value1, column2 = value2, ...WHERE <condition>) 
    def update(self,table_name, command):
        self.cur.execute(f'UPDATE {table_name} {command};')
        self.conn.commit()
    
