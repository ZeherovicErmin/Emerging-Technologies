from flask import Flask, render_template, jsonify, request
import json
import docker

app = Flask(__name__)

#Add a item class????
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price
    


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

#Display addItem.html
@app.route('/shoppingcart', methods=['GET'])
def showAddItemPage():
    return render_template('addItem.html')
#add a product to the shopping cart. If the item already exists, increiment.
@app.route('/shoppingcart', methods=['POST'])
def addItem():
    global shoppingCart
    container = run_docker_container('hl5846/products', {'80/tcp': 80})
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
    container.stop()
    container.remove()

def addToCart(item):
    global shoppingCart
    item_name = item['productName']
    item_price = item['productPrice']
    
    # Create an instance of the Item class with the parsed information
    item_instance = Item(item_name, item_price)

    # Check if the item already exists in the shopping cart
    for i, (cart_item, quantity) in enumerate(shoppingCart):
        if cart_item.name == item_instance.name:
            shoppingCart[i] = (cart_item, quantity + 1)
            break
    else:
        # If the item doesn't exist in the shopping cart, add it
        shoppingCart.append((item_instance, 1))


# Display checkout.html
@app.route('/checkout', methods=['GET'])
def checkoutPage():
    return render_template('checkout.html')

@app.route('/checkout', methods=['POST'])
def print_items():
    global shoppingCart
    cart_items = []
    for item, quantity in shoppingCart:
        cart_items.append(f"Item: {item.get_name()}, Quantity: {quantity}")
    return render_template('checkout.html', items=cart_items)

def removeItem():
    prod = 0
def totalPrice():    
    prod =0

def checkOut():
    prod =0

def run_docker_container(image_name, port_mapping):
    # Create a Docker client using the environment variables or default settings
    client = docker.from_env()
    
    # Run the Docker container with the specified image name and port mapping
    container = client.containers.run(image_name, detach=True, ports=port_mapping)
    
    # Return the container instance, in case you need to interact with it later
    return container

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
