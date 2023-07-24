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