from flask import Flask, jsonify, request, render_template, json
app = Flask(__name__)

# An Application that utilizes python and HTML to create a user registration/login system.


# An Array to store any created users information 
userList = []

# Creating a json file to store the data from our array
storage = "userList.json"

# Creating a function to load userlist to prevent duplicate users created

def loadUserList():
    with open(storage, "r") as json_file:
        return json.load(json_file)

# We will use the /user with methods of POST and GET to either get user information or display it respectively
@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return jsonify(userList), 200
    elif request.method == 'POST':
        data = request.get_json
        if 'username' in data and 'password' in data:
            # Check if the username is already taken
            if any(user['username'] == data['username'] for user in userList):
                return jsonify({'message': 'That Username is already taken'}), 400

            # Creating a new user 
            new_user = {
                'Account #': len(userList) + 1,
                'Username': data['username'],
                'Password': data['password']
            }
            userList.append(new_user)
            
            with open(storage, "a") as json_file:
                json.dump(new_user, json_file)

            return jsonify({'message': 'User created successfully'}), 201
        else:
            return jsonify({'message': 'Username and password are required'}), 400
        

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
