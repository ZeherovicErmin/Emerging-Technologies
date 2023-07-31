from flask import Flask, jsonify, request, render_template, json
import os
app = Flask(__name__)
import configparser
import requests
import chardet

config = configparser.ConfigParser()
config.read('config.ini')

# An Application that utilizes python and HTML to create a user registration/login system.


# An Array to store any created users information 
userList = []

# Creating a variable to store the json filepath
storage = "userList.json"

# Creating a userList.json file if it doesn't exist already
if not os.path.exists(storage):
    with open(storage, "w") as json_file:
        json.dump([],json_file)
            
# Populating our array with users already created
with open(storage, "r") as json_file:
    userList = json.load(json_file)




# We will use the /user with methods of POST and GET to either get user information or display it respectively
@app.route('/user', methods=['GET', 'POST'])
def user():
    id=100;
    if request.method == 'GET':
        return jsonify(userList), 200
    elif request.method == 'POST':
        data = request.form
        if 'username' in data and 'password' in data:
            
            # Ensuring duplicate usernames aren't created
            for user in userList:
                if user['username'] == data['username']:
                    return jsonify({'message': 'Username already taken!'},400)
                
            id+=1;
            # Creating a new user
            userId="U"+ str(id)
            new_user = {
                'userID': userId,
                'username': data['username'],
                'password': data['password'],
                'emailID' : data['emailID'],
                'phoneNumber' : data['phoneNumber']
            }
            userList.append(new_user)
            
            with open(storage, "w") as json_file:
                json.dump(userList, json_file)

            return render_template('success.html',userID=userId ),200
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
    ratings_url = config.get('Settings', 'ratings_url')
    print(str(orders_url)+str(userID))
    response = requests.get(orders_url+userID)

    payments_url = config.get('Settings', 'payments_url')
    payment_response = requests.get(payments_url+userID)
    payment_info = payment_response.json()


    print("payment information")
    print(payment_info)

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
                   prod_id=product[0].get('productID')
                   if( len(product) > 0 and prod_id==order.get('productID')):

                        ratings_response = requests.get(ratings_url + prod_id)
                        ratings_info = ratings_response.json()
                        order['products'] = product
                        #calculate total price and add it to the json
                        order['Total_price'] = float(product[0].get('productPrice')) * float(order.get('quantity'))
                        del order['productID']
                        order['Payment_details'] = payment_info
                        order['cyberSecurityRiskRating']= ratings_info.get("")

        print(len(orders_info))


        return orders_info
    else:
        return f"Error: {response.status_code} - {response.text}"



@app.route('/', methods=['GET'])
def index():
    return render_template('user.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
