from db import UserDb
from flask import Flask, jsonify, request
from models import User


db = UserDb()
# Create a cursor object to execute SQL queries
cursor = db.cursor

#init app
app = Flask("app")

# Define a route to get data from the database

# COMMIT BASEL ------------------- BSPMC2329-27 ---------------------------------------
@app.route('/login',methods=['POST'])
def login():
    temp = User()
    temp.email, temp.password = request.form['email'],request.form['password']
    if db.login(temp):
        user = db.get_user_by_email(temp.email).totuple()
        return jsonify({'message': 'Login successful','user': user})
    else:
        return jsonify({'message': 'Invalid username or password'})
# end  COMMIT BASEL ------------------- BSPMC2329-27 ---------------------------------------

# COMMIT adan ------------------- BSPMC2329-6 ---------------------------------------
@app.route('/register',methods=['POST'])
def register():
    temp = User()
    temp.insert(request.form['email'],request.form['password'],request.form['firstname'],request.form['Last_name'])
    if db.insert_user(temp):
        return jsonify({'message': 'register successful'})
    else:
        return jsonify({'message': 'register not successful'})
# end COMMIT adan ------------------- BSPMC2329-6 ---------------------------------------

# COMMIT adan ------------------- BSPMC2329-7 ---------------------------------------
@app.route('/user',methods=['POST'])
def user():
    id = request.form['id']
    user = db.get_user_by_id(int(id))
    if user:
        return jsonify({'message': 'register successful', 'user': user.totuple()})
    else:
        return jsonify({'message': 'register not successful'})
# end COMMIT adan ------------------- BSPMC2329-7 ---------------------------------------
@app.route('/changeType',methods =['POST'])
def change_type():
    email, type = request.form['email'], request.form['type']
    flag = db.change_type_of_user(email, type)
    if flag:
        return jsonify({'message': 'change successful'})
    else:
        return jsonify({'message': 'change not successful'})

@app.route('/changePassword',methods=['POST'])
def change_Password():
    email, new_password = request.form['email'], request.form['new_password']
    flag = db.change_password(email,new_password)
    if flag:
        return jsonify({'message': 'change successful'})
    else:
        return jsonify({'message': 'change not successful'})

@app.route('/getAllUsers',methods=['GET'])
def get_all_users():
    users = db.print_user_table()
    return jsonify({'message': 'change successful','users':users})

@app.route('/changeInfo',methods=['POST'])
def change_info():
    if db.update_info(request.form['email'],request.form['name'],request.form['lastname']):
        return jsonify({'message': 'change successful'})
    else:
        return jsonify({'message': 'change not successful'})

@app.route('/getUsersTypes',methods=['GET'])
def get_users_types():
    tupple_lst = db.get_users_types()
    return jsonify({'message': 'change successful', 'users': tupple_lst})

@app.route('/removeUser',methods = ['Post'])
def delete_user_email():
    if db.delete_user_by_email(request.form['email']):
        return jsonify({'message': 'change successful'})
    else:
        return jsonify({'message': 'change not successful'})
if __name__ == '__main__':
    app.run(debug=True)