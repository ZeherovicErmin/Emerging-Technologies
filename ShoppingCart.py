from flask import Flask, render_template, request, redirect, jsonify
import requests
import json
import urllib.request
app = Flask(__name__)

# Add an item class
class Item:
    def __init__(self, name, price, ID):
        self.name = name
        self.price = price
        self.ID = ID

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price
    
    def get_id(self):
        return self.ID

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
            price = totalPrice()
            return render_template('index.html', message=f"Total: ${price:.2f}")
        elif action == '4':
            return checkout()
        else:
            return render_template('index.html', message="Invalid action")
    else:
        return render_template('index.html', message="")

# Display addItem.html
@app.route('/shoppingcart', methods=['GET'])
def showAddItemPage():
    return render_template('addItem.html')
# Add a product to the shopping cart. If the item already exists, increment.
@app.route('/shoppingcart', methods=['POST'])
def addItem():
    global shoppingCart
    chosenItem = request.form.get('chosenItem')
    if chosenItem == '1':
        item = get_products_from_products_microservice("Laptop")
    elif chosenItem == '2':
        item = get_products_from_products_microservice("Cookware%20Set")
    elif chosenItem == '3':
        item = get_products_from_products_microservice("Hiking%20Backpack")
    elif chosenItem == '4':
        item = get_products_from_products_microservice("Smartphone")
    elif chosenItem == '5':
        item = get_products_from_products_microservice("Fitness%20Tracker")
    elif chosenItem == '6':
        item = get_products_from_products_microservice("Scented%20Candle%20Set")
    else:
        return render_template('addItem.html', message="Failed to add item")

    addToCart(item)
    return render_template('addItem.html', message="Item has been added")
    

def addToCart(item):
    global shoppingCart

    product_info = item[0]
    item_name = product_info['productName']
    item_price = product_info['productPrice']
    item_ID = product_info['productID']

    item_instance = Item(item_name, item_price, item_ID)

    # Check if the item already exists in the shopping cart
    for i, (cart_item, quantity) in enumerate(shoppingCart):
        if cart_item.ID == item_instance.ID:
            shoppingCart[i] = (cart_item, quantity + 1)
            break
    else:
        shoppingCart.append((item_instance, 1))
    

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    global shoppingCart

    items_list = []
    for item, quantity in shoppingCart:
        item_info = {
            'name': item.get_name(),
            'price': item.get_price(),
            'quantity': quantity
        }
        items_list.append(item_info)

    return jsonify(items_list)



# Display removeItem.html
@app.route('/removeshoppingcart', methods=['GET'])
def showRemoveItemPage():
    return render_template('removeItem.html')

# Remove a product from the shopping cart.
@app.route('/removeshoppingcart', methods=['POST'])
def removeItem():
    global shoppingCart
    chosenItem = request.form.get('chosenItem')
    if chosenItem:
        removeFromList(chosenItem)
        return render_template('removeItem.html', message="Item has been removed")
    else:
        return render_template('removeItem.html', message="Failed to remove item")

#if item has more than one, decriment. Other wise outright remove from list.
def removeFromList(chosenItem):
    global shoppingCart
    for i, (item, quantity) in enumerate(shoppingCart):
        if item.ID == chosenItem:
            if quantity > 1:
                shoppingCart[i] = (item, quantity - 1)
            else:
                shoppingCart.pop(i)
            break

def totalPrice():
    global shoppingCart
    total = 0
    for item, quantity in shoppingCart:
        total += item.get_price() * quantity
    return total

#NOTE: for this, have the products.py application running on port 80, if needed you can change the productsUrl to whatever else link.
#If you do change the url, make sure the fields match such as productName, productId, and productPrice.
def get_products_from_products_microservice(productName):
    productsUrl = f'http://localhost:80/product?name={productName}'
    try:
        response = requests.get(productsUrl)

        if response.status_code == 200:
            product = response.json()
            return product

        elif response.status_code == 404:
            return "Product not found."
        else:
            return f"Error: {response.status_code} - {response.reason}"
            
    except requests.exceptions.RequestException as e:
        return "Error connecting to the microservice: " + str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10)
