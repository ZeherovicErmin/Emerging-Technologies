import configparser
import random

import requests
from flask import Flask, request, jsonify, make_response, render_template

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')


@app.route("/Receipt", methods=['GET'])
def ratings():
    return render_template('receipt.html')

@app.route("/receipt/order/<orderID>")
def getReceipt(orderID):
    receiptNum=100
    try:
        orderID = request.view_args['orderID']
        orders_url = config.get('Settings', 'orders_url')
        products_url = config.get('Settings', 'products_url')
        response = requests.get(orders_url+orderID)
        data = response.json()
        order=data[0]
        productID=order['productID']
        product_info=requests.get(products_url+productID).json()
        product = product_info[0]
        receiptNum+=1;
        receipt = {
        "reciptNumber" : "R" + str(receiptNum),
        "orderID" : orderID,
        "productName": product['productName'],
        "price" : product['productPrice'],
        "totalPrice" : float(order['quantity']) * float(product['productPrice'])
        }
        return receipt;

    except Exception as e:
        return jsonify({"message":"Error while finding order informations. Please check the order ID provided"}), 500

if __name__ == '__main__':
    app.run(debug=True)
