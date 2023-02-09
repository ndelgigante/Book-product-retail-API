import pandas as pd
import mysql.connector

class DatabaseManager:
    def __init__(self):
        #requires editing to connection to actually access the database
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootroot",
        database="Book"
        )
        self.cur = conn.cursor()

    def get_df(self,table_name):
        self.cur.execute(f'SELECT * FROM {table_name}')
        table_rows = self.cur.fetchall()
        df = pd.DataFrame(table_rows)
        return df
    
