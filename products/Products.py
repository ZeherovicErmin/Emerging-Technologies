#-----------------------------------------------
# Display Technology Products Microservice
# has a JSON file with a few different products
# (can be changed to something else if needed)
#-----------------------------------------------

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

class Products:
    # Class variables
    productID = None
    productName = None
    productPrice = None
    productRating = None
    productDesc = None
    productImage = None
    isComputer = None
    isKitchenware = None
    isOutdoor = None
    isHygiene = None
    isOther = None

    # Constructor
    def __init__(self, productID, name, price, rating, desc, image, computer, kitchenware, outdoor, hygiene, other):
        self.productID = productID
        self.productName = name
        self.productPrice = price
        self.productRating = rating
        self.productDesc = desc
        self.productImage = image
        self.isComputer = computer
        self.isKitchenware = kitchenware
        self.isOutdoor = outdoor
        self.isHygiene = hygiene
        self.isOther = other

    # Getter methods
    def getProductID(self):
        return self.productID

    def getProductName(self):
        return self.productName

    def getProductPrice(self):
        return self.productPrice

    def getProductRating(self):
        return self.productRating

    def getProductDesc(self):
        return self.productDesc

    def getProductImage(self):
        return self.productImage

    def getIsComputer(self):
        return self.isComputer

    def getIsKitchenware(self):
        return self.isKitchenware

    def getIsOutdoor(self):
        return self.isOutdoor

    def getIsHygiene(self):
        return self.isHygiene

    def getIsOther(self):
        return self.isOther

    # Instance Methods

    def printProdInfo(self):  
        print("Product ID:", self.getProductID(),
              "\nProduct Name:", self.getProductName(),
              "\nPrice: $", self.getProductPrice(),
              "\nProduct Rating:", self.getProductRating(),
              "\nProduct Description:", self.getProductDesc(),
              "\nProduct Image:", self.getProductImage())

@app.route('/')
def main():
    products = loadJson()
    return jsonify(displayProducts(products))

def loadJson():
    # Read JSON file
    with open('productList.json') as file:
        data = json.load(file)

    # Access JSON file into array and create a list to host parsed info
    productsData = data['products']
    products = []

    # Iterate over json file into array
    for productInfo in productsData:
        product_id = productInfo['productID']
        product_name = productInfo['productName']
        product_price = productInfo['productPrice']
        product_rating = productInfo['productRating']
        product_desc = productInfo['productDesc']
        product_image = productInfo['productImage']
        is_computer = productInfo['isComputer']
        is_kitchenware = productInfo['isKitchenware']
        is_outdoor = productInfo['isOutdoor']
        is_hygiene = productInfo['isHygiene']
        is_other = productInfo['isOther']

        # Create an instance of the Products class with the parsed information
        product = Products(product_id, product_name, product_price, product_rating, product_desc, product_image, is_computer, is_kitchenware, is_outdoor, is_hygiene, is_other)

        # Add the product to the list of products
        products.append(product)
    return products

#Can add for example (/product?name=Laptop) at the end of link and return laptop information
@app.route('/product', methods=['GET'])
def get_specific_product():
    desired_product_name = request.args.get('name')  
    products = loadJson()  
    found_products = []
    for product in products:
        if product.getProductName() == desired_product_name:
            found_products.append({
                'productID': product.getProductID(),
                'productName': product.getProductName(),
                'productPrice': product.getProductPrice(),
                'productRating': product.getProductRating(),
                'productDesc': product.getProductDesc(),
                'productImage': product.getProductImage()
            })
    return jsonify(found_products)


#find product details by product ID
@app.route('/product/<productID>', methods=['GET'])
def get_product_by_id(productID):
    product_id = request.view_args['productID']
    products = loadJson()
    found_products = []
    for product in products:
        if product.getProductID() == product_id:
            found_products.append({
                'productID': product.getProductID(),
                'productName': product.getProductName(),
                'productPrice': product.getProductPrice(),
                'productRating': product.getProductRating(),
                'productDesc': product.getProductDesc(),
                'productImage': product.getProductImage()
            })
    return jsonify(found_products)


def displayProducts(products):
    product_info = []
    for product in products:
        product_info.append({
            'productID': product.getProductID(),
            'productName': product.getProductName(),
            'productPrice': product.getProductPrice(),
            'productRating': product.getProductRating(),
            'productDesc': product.getProductDesc(),
            'productImage': product.getProductImage()
        })
    return product_info

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
