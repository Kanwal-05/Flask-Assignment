# C. Show Electronics items – GET – This method will return all the electronics from a static dictionary as a JSON response 
from flask import Flask , jsonify
app=Flask("Project 2")

data=[
    {
        "Product_id":1,
        "Product_name":"Smartphone",
        "Product_desc":"6.5-inch screen, 5G",
        "Product_cost": 499.99,
        "Product_catagory":"Electrionics",
        "Quantity_available":100
    },
    {
        "Product_id":2,
        "Product_name":"Sneakers",
        "Product_desc":"Running Shoes, Size 10",
        "Product_cost": 89.99,
        "Product_catagory":"Footwear",
        "Quantity_available":50
    },
    {
        "Product_id":3,
        "Product_name":"T-Shirt",
        "Product_desc":"Cotton Fabric, XL",
        "Product_cost": 19.99,
        "Product_catagory":"Clothing",
        "Quantity_available":200
    },
    {
        "Product_id":4,
        "Product_name":"Wireless Earbuds",
        "Product_desc":"Bluetooth, Noise Cancellation",
        "Product_cost": 129.99,
        "Product_catagory":"Electrionics",
        "Quantity_available":75
    },   
    {
        "Product_id":5,
        "Product_name":"Backpack",
        "Product_desc":"Water Resistant, Laptop Sleeve",
        "Product_cost": 79.99,
        "Product_catagory":"Accessories",
        "Quantity_available":40
    }
]

@app.route("/products", methods=["GET"])
def get_user():
    return jsonify(data)

@app.route("/products/electronics", methods=["GET"])
def electronics():
    electronics_products = []

    for product in data:
        if product["Product_catagory"] == "Electrionics":
            electronics_products.append(product)

    return jsonify(electronics_products)


if __name__=="__main__":
    app.run(debug=True)