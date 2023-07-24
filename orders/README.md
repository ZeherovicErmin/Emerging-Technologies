Orders microservice to fetch order details: 

Order json document sample and fields :
  {
      "orderID": "O12345",
      "productID": "P789",
      "quantity": 10,
      "userID": "U444"
  }


Endpoints and details : 

1. To fetch all the order details
   method : GET
   endpoint : {{hosturl}}/orders/allOrders
   
2. To fetch order details based on orderID
   method : GET
   endpoint : {{hosturl}}/orders/<orderID>

3. To fetch order details based on orderID
   method : GET
   endpoint : {{hosturl}}/orders/user/<userID>

3. To add new order details 
   method : POST
   endpoint : {{hosturl}}/orders/addNewOrder'
   sample json object for post request:
     
   

