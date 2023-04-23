from db import UserDb
from flask import Flask, jsonify, request
from models import User


db = UserDb()
# Create a cursor object to execute SQL queries
cursor = db.cursor

#init app
app = Flask("app")

@app.route('/login',methods=['POST'])
def login():
    temp = User()
    temp.email, temp.password = request.form['email'],request.form['password']
    if db.login(temp):
        user = db.get_user_by_email(temp.email).totuple()
        return jsonify({'message': 'Login successful','user': user})
    else:
        return jsonify({'message': 'Invalid username or password'})

if __name__ == '__main__':
    app.run(debug=True)