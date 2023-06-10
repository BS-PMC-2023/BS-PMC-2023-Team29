from db import Db
from flask import Flask, jsonify, request
from models import User

db = Db()

# Create a cursor object to execute SQL queries
cursor = db.cursor

# init app
app = Flask("app")


@app.route('/login', methods=['POST'])
def login():
    temp = User()
    temp.email, temp.password = request.form['email'], request.form['password']
    if db.login(temp):
        user = db.get_user_by_email(temp.email).totuple()
        return jsonify({'message': 'Login successful', 'user': user})
    else:
        return jsonify({'message': 'Invalid username or password'})


@app.route('/register', methods=['POST'])
def register():
    temp = User()
    temp.insert(request.form['email'], request.form['password'], request.form['firstname'], request.form['lastname'])
    if db.insert_user(temp):
        return jsonify({'message': 'register successful'})
    else:
        return jsonify({'message': 'register not successful'})


@app.route('/user', methods=['POST'])
def user():
    id = request.form['id']
    user = db.get_user_by_id(int(id))
    if user:
        return jsonify({'message': 'register successful', 'user': user.totuple()})
    else:
        return jsonify({'message': 'register not successful'})


@app.route('/changeType', methods=['POST'])
def change_type():
    email, type = request.form['email'], request.form['type']
    flag = db.change_type_of_user(email, type)
    if flag:
        return jsonify({'message': 'change successful'})
    else:
        return jsonify({'message': 'change not successful'})


@app.route('/changePassword', methods=['POST'])
def change_Password():
    email, temp_password, new_password = request.form['email'], request.form['temp_password'], request.form[
        'new_password']
    flag = db.change_password(email, temp_password, new_password)
    if flag:
        return jsonify({'message': 'change successful'})
    else:
        return jsonify({'message': 'change not successful'})


@app.route('/getAllUsers', methods=['GET'])
def get_all_users():
    users = db.print_user_table()
    return jsonify({'message': 'change successful', 'users': users})


@app.route('/changeInfo', methods=['POST'])
def change_info():
    if db.update_info(request.form['email'], request.form['name'], request.form['lastname']):
        return jsonify({'message': 'change successful'})
    else:
        return jsonify({'message': 'change not successful'})


@app.route('/getUsersTypes', methods=['GET'])
def get_users_types():
    tupple_lst = db.get_users_types()
    return jsonify({'message': 'change successful', 'users': tupple_lst})


@app.route('/removeUser', methods=['POST'])
def delete_user_email():
    if db.delete_user_by_email(request.form['email']):
        return jsonify({'message': 'change successful'})
    else:
        return jsonify({'message': 'change not successful'})


@app.route('/getAllSupply', methods=['GET'])
def get_all_supply():
    supply = db.get_all_supply()
    return jsonify({'message': 'successful', 'supply': supply})


@app.route('/getAllBorrows', methods=['GET'])
def get_all_borrows():
    user_id = (request.form['user_id'])
    borrows = db.get_all_my_borrows(user_id)
    return jsonify({'message': 'successful', 'borrows': borrows})


@app.route('/getLateReturns', methods=['GET'])
def get_late_returns():
    late_returns = db.get_late_returns()
    if late_returns:
        # Assuming the returned format from db.get_late_returns() is a list of tuples
        # where each tuple represents (borrow_id, item_id, user_id, num_of_items, borrow_date, expected_return, real_return)
        return jsonify({
            'message': 'successful',
            'late_returns': [{
                'borrow_id': lr[0],
                'item_id': lr[1],
                'user_id': lr[2],
                'num_of_items': lr[3],
                'borrow_date': lr[4].strftime('%a, %d %b %Y %H:%M:%S %Z'),
                'expected_return': lr[5].strftime('%a, %d %b %Y %H:%M:%S %Z'),
                'real_return': lr[6].strftime('%a, %d %b %Y %H:%M:%S %Z') if lr[6] else None,
            } for lr in late_returns]
        })
    else:
        return jsonify({'message': 'No late returns found.'})


@app.route('/borrowItem', methods=['POST'])
def borrow_item():
    # get values from form data
    user_id = (request.form['user_id'])
    item_id = request.form['item_id']
    return_time = request.form['return_time']
    num_of_items = request.form['num_of_items']
    num_of_items_remain = request.form['num_of_items_remain']

    # pass to db.borrow_item function
    if db.borrow_item(user_id, item_id, return_time, num_of_items, num_of_items_remain):
        return jsonify({'message': 'Borrowing item successful'})
    return jsonify({'message': 'Borrowing item not successful'})


@app.route('/returnAllItems', methods=['POST'])
def return_all_items():
    if db.return_all_items(request.form['user_id']):
        return jsonify({'message': 'change successful'})
    return jsonify({'message': 'change not successful'})


@app.route('/returnSomeItem', methods=['POST'])
def return_some_items():
    if db.return_all_items(request.form['user_id']):
        return jsonify({'message': 'change successful'})
    return jsonify({'message': 'change not successful'})


@app.route('/generateTempPassword', methods=['POST'])
def generate_temp_password():
    if db.generate_temp_password(request.form['email']):
        return jsonify({'message': 'change successful'})
    return jsonify({'message': 'change not successful'})


@app.route('/getBorrowedItems', methods=['POST'])
def get_my_borrowed_items():
    items = db.get_items_dosent_return(request.form['user_id'])
    return jsonify({'message': 'successful', 'items': items})


@app.route('/addItemToSupply', methods=['POST'])
def add_item_to_supply():
    item_id = db.add_item_to_supply(request.form['name'], request.form['units'], request.form['type'],
                                    request.form['description'])
    if item_id:
        return jsonify({'message': 'change successful', 'id': item_id})
    return jsonify({'message': 'change not successful'})


@app.route('/plot_borrow', methods=['GET'])
def plot_borrow():
    borrow_data, num_of_items = db.plot_borrow()
    print(borrow_data)
    print(num_of_items)
    return jsonify({'borrow_data': borrow_data, 'num_of_items': num_of_items})


@app.route('/reportItem', methods=['POST'])
def report_item():
    if db.report_problem_item(request.form['user_id'], request.form['id'], request.form['des'], request.form['units']):
        return jsonify({'message': 'change successful'})
    return jsonify({'message': 'change not successful'})


@app.route('/getPendingOrders', methods=['GET'])
def get_pending_orders():
    pending_orders = db.get_pending_borrows()
    if pending_orders:
        # Assuming the returned format from db.get_pending_orders() is a list of tuples
        # where each tuple represents (borrow_id, item_id, user_id, num_of_items, borrow_date, expected_return, real_return)
        return jsonify({
            'message': 'successful',
            'pending_orders': [{
                'borrow_id': ord[0],
                'item_id': ord[1],
                'user_id': ord[2],
                'num_of_items': ord[3],
                'borrow_date': ord[4].strftime('%a, %d %b %Y %H:%M:%S %Z'),
                'expected_return': ord[5].strftime('%a, %d %b %Y %H:%M:%S %Z'),
                'real_return': ord[6].strftime('%a, %d %b %Y %H:%M:%S %Z') if ord[6] else None,
            } for ord in pending_orders]
        })
    else:
        return jsonify({'message': 'No pending orders found.'})


@app.route('/approveOrder', methods=['POST'])
def approve_order():
    borrow_id = request.form['borrow_id']
    result = db.approve_order(borrow_id)
    if result:
        return jsonify({'message': 'Order approved successfully'})
    else:
        return jsonify({'message': 'Failed to approve order'})


@app.route('/getUserData', methods=['GET'])
def get_user_data():
    user_id = request.args.get('user_id')
    user_type = request.args.get('user_type')

    if user_type == '1':
        borrowed_items = db.get_borrowed_items(user_id)
        closest_return_date = db.get_closest_return_date(user_id)
        pending_orders = db.get_pending_orders(user_id)
        approved_orders = db.get_approved_orders(user_id)

        return jsonify({
            'borrowed_items': borrowed_items if borrowed_items is not None else 0,
            'closest_return_date': closest_return_date if closest_return_date is not None else 0,
            'pending_orders': pending_orders if pending_orders is not None else 0,
            'approved_orders': approved_orders if approved_orders is not None else 0,
        })

    elif user_type == '3':
        total_borrowed_items = db.get_total_borrowed_items()
        total_late_returns = db.get_total_late_returns()
        total_users = db.get_total_users()
        total_items = db.get_total_items()

        return jsonify({
            'total_borrowed_items': total_borrowed_items if total_borrowed_items is not None else 0,
            'total_late_returns': total_late_returns if total_late_returns is not None else 0,
            'total_users': total_users if total_users is not None else 0,
            'total_items': total_items if total_items is not None else 0,
        })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
