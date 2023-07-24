from flask import Flask,jsonify,request
app = Flask(__name__)


# An application designed to provide a user account creation/login system


@app.route('/user', methods=['GET'])

def rand_joke():
    if request.method == 'GET':
    

        
        # Gathering a variable from our url
        number = int(request.args.get('num', default=1))


        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)