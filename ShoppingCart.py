from flask import Flask, render_template, jsonify, request
import json


app = Flask(__name__)

shoppingCart = []

@app.route('/', methods=['GET', 'POST'])
def main():
    global shoppingCart
    if request.method == 'POST':
        action = request.form.get('action')
        if action == '1':
            addItem()
            return render_template('index.html', message="Add an Item")  
        elif action == '2':
            removeItem()
            return render_template('index.html', message="Remove an Item")  
        elif action == '3':
            totalPrice()
            return render_template('index.html', message="Display Total")  
        elif action == '4':
            #checkout()
            print_items()
            return render_template('index.html', message="Proceed to Checkout")  
        else:
            return render_template('index.html', message="Invalid action")
               
    else:
        return render_template('index.html', message="")  

@app.route('/shoppingcart', methods=['GET'])
def showAddItemPage():
    return render_template('addItem.html')
#add a product to the shopping cart. If the item already exists, increiment.
@app.route('/shoppingcart', methods=['POST'])
def addItem():
    global shoppingCart
    if request.method == 'POST':
        chosenItem = request.form.get('chosenItem')
        if chosenItem == '1':
            item = get_products_from_products_microservice("Laptop")
        elif chosenItem == '2':
            item = get_products_from_products_microservice("Cookware Set")
        elif chosenItem == '3':
            item = get_products_from_products_microservice("Hiking Backpack")
        elif chosenItem == '4':
            item = get_products_from_products_microservice("Smartphone")
        elif chosenItem == '5':
            item = get_products_from_products_microservice("Fitness Tracker")
        elif chosenItem == '6':
            item = get_products_from_products_microservice("Scented Candle Set")
        else:
            return render_template('addItem.html', message="Failed to add item")

    addToCart(item)
    return render_template('addItem.html', message="Item has been added")

def addToCart(item):
   global shoppingCart
   for i, (name, quantity) in enumerate(shoppingCart):
       if name == item:
           shoppingCart[i] = (name, quantity + 1)
           break
   else:
       shoppingCart.append((item, 1))

def print_items():
    global shoppingCart
    for item, quantity in shoppingCart:
        print(f"{item}: {quantity}") 

def removeItem():
    prod = 0
def totalPrice():    
    prod =0

def checkOut():
    prod =0

def get_products_from_products_microservice(productName):

    productsUrl = f'http://localhost:80/product?name={productName}'
    try:
        response = requests.get(productsUrl)

        if response.status_code == 200:
            product = response.json()
            return product
        else:
            return "Sorry, this product does not exist."

    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the HTTP request
        return "Error connecting to the microservice: " + str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10)
