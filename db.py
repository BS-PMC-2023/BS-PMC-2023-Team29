import mysql.connector
import re
from models import User
from dotenv import load_dotenv
import os
import logging as lg

class Db:
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


    # Retrieve some data from the 'customers' table
    def print_user_table(self):
        self.cursor.execute("SELECT * FROM users")
        result = self.cursor.fetchall()
        for row in result:
          lg.debug(row)
        return result

    def login(self,user):
        flag = False
        self.cursor.execute("SELECT email,password FROM users")
        result = self.cursor.fetchall()
        for i in result:
            if i[0] == user.email:
                flag = True
                if i[1] == user.password:
                    lg.debug("login worked great success")
                    return True
                else:
                    lg.debug("wrong password")
                    lg.debug("not great success")
                    return False
        if not flag:
            lg.debug('there is no email like this')
            lg.debug("not great success")
            return False

    def get_user_by_id(self,id):
        self.cursor.execute("SELECT * FROM users")
        result = self.cursor.fetchall()
        for i in result:
            if id == i[0]:
                user = User()
                user.tupple_insert(i)
                lg.debug(user)
                return user
        return False

    def get_user_by_email(self,email):
        self.cursor.execute("SELECT * FROM users")
        result = self.cursor.fetchall()
        for i in result:
            if email == i[1]:
                user = User()
                user.tupple_insert(i)
                lg.debug(user)
                return user
        return False

    def change_type_of_user(self,email,type):
        query = "UPDATE users SET type = %s WHERE email = %s"
        self.cursor.execute(query,(type,email))
        self.mydb.commit()
        return True

    def change_password(self,email,newpassword):
        query = "UPDATE users SET password = %s WHERE email = %s"
        self.cursor.execute(query, (newpassword, email))
        self.mydb.commit()
        return True

    def update_info(self,email,name,lastname):
        id = self.get_user_by_email(email).id
        query = "UPDATE users SET email=%s,name=%s,lastname =%s WHERE id = %s"
        self.cursor.execute(query, (email,name, lastname,id))
        self.mydb.commit()
        return True

    def get_users_types(self):
        self.cursor.execute("SELECT email,type FROM users")
        result = self.cursor.fetchall()
        return result

    def delete_user_by_email(self, email):
        query = "DELETE FROM users WHERE email = %s"
        self.cursor.execute(query, (email))
        self.mydb.commit()
        return True

    def get_all_supply(self):
        self.cursor.execute("SELECT * FROM supply")
        result = self.cursor.fetchall()
        for row in result:
            lg.debug(row)
        return result

#-------- test db model ---------------
# db = Db()
# # Create a cursor object to execute SQL queries
# cursor = db.cursor
# print(db.get_all_supply())