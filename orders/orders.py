from flask import Flask, jsonify, request
import json

app = Flask(__name__)

class Orders:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
    # Class variables
    orderID = None
    productID = None
    userID = None
    quantity = None

    # Constructor
    def __init__(self, orderID,productID, userID, quantity):
        self.orderID=orderID
        self.productID = productID
        self.userID = userID
        self.quantity = quantity

        # Getter methods
        def getProductID(self):
            return self.productID

        def getOrderID(self):
            return self.orderID

        def getUserID(self):
            return self.userID

        def getQuantity(self):
            return self.quantity

        def displayOrders(orders):
            order_info = []

            if (type(orders) == list.__class__):
                for order in orders:
                    order_info.append({
                        'orderID': order.getOrderID(),
                        'productID': order.getProductID(),
                        'userID': order.getUserID(),
                        'quantity': order.getQuantity()

                    })
            else:
                order_info.append({
                    'orderID': orders.getOrderID(),
                    'productID': orders.getProductID(),
                    'userID': orders.getUserID(),
                    'quantity': orders.getQuantity()

                })
            return order_info

        def load_json():
            with open("./static/orders.json", "r") as file:
                data = json.load(file)
            return data

        def save_json(data):
            with open("./static/orders.json", "w") as file:
                json.dump(data, file, indent=2)

        def loadJsonAsList():
            # Read JSON file
            with open('./static/orders.json', 'r') as file:
                data = json.load(file)

            # Access JSON file into array and create a list to host parsed info
            ordersInfo = data['orders']
            orders = []

            # Iterate over json file into array
            for orderdetail in ordersInfo:
                order_id = orderdetail['orderID']
                product_id = orderdetail['productID']
                user_id = orderdetail['userID']
                quantity = orderdetail['quantity']

                # Create an instance of the Products class with the parsed information
                order = Orders(order_id, product_id, user_id, quantity)

                # Add the order to the list of orders
                orders.append(order)

            return orders