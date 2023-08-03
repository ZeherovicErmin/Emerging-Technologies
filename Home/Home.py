import random
from flask import Flask, request, jsonify, make_response, render_template

app = Flask(__name__)


@app.route("/Home", methods=['GET'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
