from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route("/shoesshop")
def get_data_from_ShoesShop():
    """ Returns data from Shoes Shop's orders database which fulfill search conditions passed by arguments. 
    Will also return error message in case of query/connection errors.
    Query construction example - http://127.0.0.1:5000/shoesshop?email=b@b.com&order_number=1230 
    Also deployed as a Linode's container at http://172.105.244.153:5000 """

    email = request.args.get('email')
    order_number = request.args.get('order_number')
    result =0
    try:
        ss_data = requests.get("https://customizations.chatbotize.com/ecommerce/orders", 
            headers={"X-API-KEY": "c895a35c365541c4ac22a61d13bc388d"})
        ss_data_json = ss_data.json()
    finally:
        if ss_data.status_code == 200:
            for item in ss_data_json["items"]:
                if item["email"] == email and item["orderNumber"] == order_number:
                    result = item
                    return result
            if result == 0:
                return  {
                "Error message": "No record found in Shoes Shop orders database", 
                 }
        else:
            return {
                "Error message": "ShoesShop database not accessible", 
                "Error code" : ss_data.status_code
                }
