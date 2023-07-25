from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

# An Application that utilizes python and HTML to create a user registration/login system.


# An Array to store any created users information 
userList = []


# We will use the /user with methods of POST and GET to either get user information or display it respectively
@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return jsonify(userList), 200
    elif request.method == 'POST':
        data = request.form
        if 'username' in data and 'password' in data:
            # Check if the username is already taken
            if any(user['username'] == data['username'] for user in users):
                return jsonify({'message': 'Username already taken'}), 400

            new_user = {
                'id': len(userList) + 1,
                'username': data['username'],
                'password': data['password']
            }
            userList.append(new_user)
            return jsonify({'message': 'User created successfully'}), 201
        else:
            return jsonify({'message': 'Username and password are required'}), 400

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
