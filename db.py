import mysql.connector
import re
from models import User
from dotenv import load_dotenv
import os
import logging as lg

class UserDb:
    # Connect to the MySQL database
    def __init__(self):
        load_dotenv()
        host, user, password, database= os.getenv('HOST'),os.getenv('USER'),os.getenv('PASSWORD'),os.getenv('DATABASE')

        self.mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
        )
        lg.info('db connect great success')
        self.cursor = self.mydb.cursor()

    def __enter__(self):
        self.cursor = self.mydb.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()

    # Create a table named Users
    def create_user_table(self):
        self.cursor.execute("CREATE TABLE Users (id INT AUTO_INCREMENT PRIMARY KEY , email VARCHAR(255) , password VARCHAR(255) , type int(2) , name VARCHAR(255) , lastname VARCHAR(255))")
    def insert_user(self,user):
        query = "INSERT INTO users (email, password,type,name,lastname) VALUES (%s, %s,%s, %s,%s)"

        #check if valid email
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.search(regex, user.email):
            lg.debug('not a valid email')
            lg.debug("not great success")
            return False

        #check if there is username with this email
        self.cursor.execute("SELECT email FROM users")
        result = self.cursor.fetchall()
        for i in result:
            if i[0] == user.email:
                lg.debug(f'there is {user.email} in db')
                lg.debug("not great success")
                return False

        #insert
        self.cursor.execute(query,user.totuple())
        self.mydb.commit()
        lg.debug(self.cursor.rowcount, "record(s) inserted.")
        lg.debug("great success")
        return True