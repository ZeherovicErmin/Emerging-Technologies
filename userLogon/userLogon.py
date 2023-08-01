import requests
from flask import Flask, jsonify, request, render_template, json, redirect, url_for
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
    data = request.get_json()
    

    if 'username' in data and 'password' in data:
        
        
        # Test cases for logon services
        
        for user in userList:
            print(user['username'])
            print(data.get('username'))
            print(user['password'])
            # All correct
            if user['username'] == data.get('username') and user['password'] == data.get('password'):
                print("success")
                return jsonify({'message':'succesfull logged in'}, 200)

    # Return statement if username/password is incorrect       
    return jsonify({'message': 'Username or password is incorrect.'},401) 
    
         
                
                
# Using an Html with a template to display a front end for login
@app.route('/', methods=['GET'])
def loginT():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11000, debug=True)