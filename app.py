from db import UserDb
from flask import Flask, jsonify, request
from models import User


db = UserDb()
# Create a cursor object to execute SQL queries
cursor = db.cursor

#init app
app = Flask("app")

if __name__ == '__main__':
    app.run(debug=True)