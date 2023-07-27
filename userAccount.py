from flask import Flask, jsonify, request, render_template, json
import os
app = Flask(__name__)

# An Application that utilizes python and HTML to create a user registration/login system.


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
            
            

# We will use the /user with methods of POST and GET to either get user information or display it respectively
@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return jsonify(userList), 200
    elif request.method == 'POST':
        data = request.form
        if 'username' in data and 'password' in data:
            
            # Ensuring duplicate usernames aren't created
            for user in userList:
                if user['Username'] == data['username']:
                    return jsonify({'message': 'Username already taken!'},400)
                
                
            # Creating a new user 
            new_user = {
                'Account #': len(userList) + 1,
                'Username': data['username'],
                'Password': data['password']
            }
            userList.append(new_user)
            
            with open(storage, "w") as json_file:
                json.dump(userList, json_file)

            return jsonify({'message': 'User created successfully'}), 201
        else:
            return jsonify({'message': 'Username and password are required'}), 400
        

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
