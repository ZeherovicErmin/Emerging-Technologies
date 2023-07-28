from flask import Flask, jsonify, request, render_template, json
import os
app = Flask(__name__)

# A simple payment processing implementation 


# An Array to store any created users information 
userList = []

# Creating a variable to store the json filepath
storage = "userList.json"

# Creating a userList.json file if it doesn't exist already
if not os.path.exists(storage):
    with open(storage, "w") as json_file:
        json.dump([],json_file)
            
# Populating our array with users already created
with open(storage, "r") as json_file:
    userList = json.load(json_file)
    
@app.route('/user/payment', methods=['POST'])

def payment():
    data = request.form
    

    if 'username' in data and 'password' in data:
        
        user_payment = {
         'Username': data['username'],
         'Password': data['password'],
         'Cardnum' : data['cardnum'],
         'Expdate' : data['expdate'],
         'CCV'     : data['ccv']
            }
    userList.append(user_payment)
    
    with open(storage, "w") as json_file:
                json.dump(userList, json_file)
                
    # Return statement if username/password is incorrect       
    return jsonify({'message': 'Your payment method has been saved succesfully.'},401)     
    
    
    
         
                
                
# Using an Html with a template to display a front end for login
@app.route('/', methods=['GET'])
def loginT():
    return render_template('payment.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)