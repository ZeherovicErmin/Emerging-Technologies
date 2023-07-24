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