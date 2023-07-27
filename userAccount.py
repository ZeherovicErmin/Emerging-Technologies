from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
import configparser
import requests
import chardet

config = configparser.ConfigParser()
config.read('config.ini')

# An Application that utilizes python and HTML to create a user registration/login system.


# An Array to store any created users information 
userList = []


# We will use the /user with methods of POST and GET to either get user information or display it respectively
@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return jsonify(userList), 200
    elif request.method == 'POST':
        data = request.form
        if 'username' in data and 'password' in data:
            # Check if the username is already taken
            if any(user['username'] == data['username'] for user in users):
                return jsonify({'message': 'Username already taken'}), 400

            new_user = {
                'id': len(userList) + 1,
                'username': data['username'],
                'password': data['password']
            }
            userList.append(new_user)
            return jsonify({'message': 'User created successfully'}), 201
        else:
            return jsonify({'message': 'Username and password are required'}), 400


@app.route('/user/orderDetails/<userID>')
def getAllOrderDetails(userID):
    order_Details=[]
    productIDs=[]
    products_info =[]
    userID = request.view_args['userID']
    orders_url = config.get('Settings', 'orders_url')
    products_url = config.get('Settings', 'products_url')
    print(str(orders_url)+str(userID))
    response = requests.get(orders_url+userID)

    if(response.status_code==200):
        orders_info=response.json()
        for order in orders_info:
            print(type(order))
            productIDs.append(order.get('productID'))

        print(productIDs)
        for productID in productIDs:
            response = requests.get(products_url + productID)
            print(products_url + productID)
            products_info.append(response.json())
            print(type(products_info))

        for order in orders_info:
            print(type(order))
            if 'productID' in order:
               for product in products_info:
                   print("product type : " , type(product))
                   print(product)
                   if(product[0].get('productID')==order.get('productID')):

                        order['products'] = product
                        #calculate total price and add it to the json
                        order['Total_price'] = float(product[0].get('productPrice')) * float(order.get('quantity'))
                        del order['productID']
        print(len(orders_info))
        return orders_info
    else:
        return f"Error: {response.status_code} - {response.text}"



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
