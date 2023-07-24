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
        elif action == '2':
            removeItem()
        elif action == '3':
            totalPrice()
        elif action == '4':
            checkOut()
        else:
            return render_template('index.html', message="Invalid action")
        return render_template('index.html', message="Action successful")  
    else:
        return render_template('index.html', message="")  



#add a product to the shopping cart. If the item already exists, increiment.
def addItem(): 
    chosenItem = input("\nWhich Product would you like to buy?\n1. Laptop\n2. Cookware Set\n3. Hiking Backpack\n4. Smartphone\n5. Fitness Tracker\n6. Scented Candle Set\nItem: ")
    if chosenItem == 1:
        item = get_products_from_products_microservice("Laptop")
    elif chosenItem == 2:
        item = get_products_from_products_microservice("Cookware Set")
    elif chosenItem == 3:
        item = get_products_from_products_microservice("Hiking Backpack")
    elif chosenItem == 4:
        item = get_products_from_products_microservice("Smartphone")
    elif chosenItem == 5:
        item = get_products_from_products_microservice("Fitness Tracker")
    elif chosenItem == 6:
        item = get_products_from_products_microservice("Scented Candle Set")
    else:
        return None
    
    addToCart(item)

def addToCart(item):
   global shoppingCart
   for i, (name, quantity) in enumerate(shoppingCart):
       if name == item:
           shoppingCart[i] = (name, quantity + 1)
           break
   else:
       shoppingCart.append((item, 1))

def print_items():
    print("items =", items)   

def removeItem():
    prod = 0
def totalPrice():    
    prod =0

def checkOut():
    prod =0

def get_products_from_products_microservice(productName):
    productsUrl = 'http://127.0.0.1:80/product?name=' + productName 
    response = requests.get(productsUrl)

    if response.status_code == 200:
        product = response.json()
        return product
    else:
        return "Sorry, this product does not exist."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10)
