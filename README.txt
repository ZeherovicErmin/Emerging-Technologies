//----------------------------------------------------------------
// ShoppingCart.py program for group 5 in microservices class
//----------------------------------------------------------------
Just some notes and a few tips for this program.

This program pulls from the products.py json file using the 'http://localhost:80/product?name={productName}' endpoint
if you wish to change it you should update the 'def get_products_from_products_microservice(productName):' method url
From the json file it pulls from 'productName, productId, and productPrice' fields aslong as you have those it will work

endpoints in this program are:
https://localhost:10/                      - Main index page displays a few buttons of actions the user can take
https://localhost:10/shoppingcart          - Displays items the user can add to their cart
https://localhost:10/removeshoppingcart    - Displays items the user can remove from their cart
https://localhost:10/checkout              - Displays the shopping cart and its contents in a json format, can add a userID and an orderID if needed.
