import random
from flask import Flask, request, jsonify, make_response, render_template, json

app = Flask(__name__)

def load_json():
    with open("ratings.json", "r") as file:
        data = json.load(file)
    return data


@app.route("/Ratings", methods=['GET'])
def ratings():
    return render_template('risk_ratings.html')




@app.route("/ratings/<productID>", methods=['GET'])
def getProductRating(productID):
    ratingsList = load_json()
    productID =request.view_args['productID']
    for rating in ratingsList:
        if(rating['productID']==productID):
            ratings = {
                'rating': rating['riskRating']
            }
            return ratings
    return "not found"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)