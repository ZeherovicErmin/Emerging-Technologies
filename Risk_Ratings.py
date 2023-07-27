import random
import json
from flask import Flask, request, jsonify, make_response, render_template

app = Flask(__name__)


@app.route("/Risk_Ratings")
def ratings():
    return render_template('Risk_Ratings.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
