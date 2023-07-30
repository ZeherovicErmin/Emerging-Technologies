import random
from flask import Flask, request, jsonify, make_response, render_template

app = Flask(__name__)


@app.route("/Home", methods=['GET'])
def ratings():
    return render_template('emergingFront.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)