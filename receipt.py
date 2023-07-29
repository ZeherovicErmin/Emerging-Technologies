import random
from flask import Flask, request, jsonify, make_response, render_template
import json
import os

app = Flask(__name__)




@app.route("/Receipt", methods=['GET', 'POST'])
def orderdisp():
    if request.method == 'POST':
        orderID = request.form.get('orderID')
        if orderID:
            order_data = receipt(orderID)
            print(order_data)
            if order_data:
                return render_template('receipt.html', orders=order_data)
                
    return render_template('orderForm.html')




def receipt(orderID):
    with open("./orders/static/orders.json", "r") as file:
        data = json.load(file)
    for order in data["orders"]:
        if order["orderID"] == orderID:
            return order
    return None



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
