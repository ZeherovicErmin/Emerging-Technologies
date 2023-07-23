from flask import Flask, jsonify, request
import json


app = Flask(__name__)

@app.route('/')
def main():
    shoppingCart = []

def addItem():

def subtractItem():

def removeItem():

def totalPrice():    

def get_products_from_products_microservice(productName):
    products_url = 'http://127.0.0.1:80/product?name=' + productName 
    response = requests.get(products_url)

    if response.status_code == 200:
        products_data = response.json()
        return products_data
    else:
        return "Sorry, this product does not exist."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10)
