import random
from flask import Flask, request, jsonify, make_response, render_template, json, url_for

app=Flask(__name__,template_folder='templates')

def load_json():
    with open("ratings.json", "r") as file:
        data = json.load(file)
    return data

def save_json(data):
    with open("ratings.json", "w") as file:
        json.dump(data, file, indent=2)

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
    return "Please check the product ID provided "

@app.route("/addratings", methods=['POST'])
def addNewRating():
    ratingsList = load_json()
    ratings = request.get_json()
    ratingsList.append(ratings)
    save_json(ratingsList)

    return jsonify("message", "ratings added successfully")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)