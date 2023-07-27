from flask import Flask, jsonify, request, render_template, json
import os
app = Flask(__name__)

# An application to simulate user login

# Creating a variable to store the json filepath
storage = "userList.json"

# Populating our array with users already created
with open(storage, "r") as json_file:
    userList = json.load(json_file)


@app.route('/user/login', methods=['POST'])

def login():
    data = request.form
    
    if 'username' in data and 'password' in data:
        
        # Test cases for logon services
        
        for user in userList:
            
            # All correct
            if user['Username'] == data['username'] and user['Password'] == data['password']:
                return jsonify({'message': 'Login Succesful!'},200)

            # Incorrect password
            if user['Password'] != data['password']:
                return jsonify({'message': 'Incorrect Password.'},401) 
            
    # Return statement that states user does not exist        
    return jsonify({'message': 'User with that Username does not exist.'},401) 
    
         
                
                
# Using an Html with a template to display a front end for login
@app.route('/', methods=['GET'])
def loginT():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)