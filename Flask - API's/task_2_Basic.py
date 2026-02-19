# B. Show Products– GET – This method will return all available products from a static dictionary as a JSON response
from flask import Flask , jsonify
app=Flask("Project 2")

data=[
    {
        "Product_id":1,
        "Product_name":"Smartphone",
        "Product_desc":"6.5-inch screen, 5G",
        "Product_cost": 499.99,
        "Product_catagory":"Electrionics",
        "Quantity_ available":100
    },
    {
        "Product_id":2,
        "Product_name":"Sneakers",
        "Product_desc":"Running Shoes, Size 10",
        "Product_cost": 89.99,
        "Product_catagory":"Footwear",
        "Quantity_ available":50
    },
    {
        "Product_id":3,
        "Product_name":"T-Shirt",
        "Product_desc":"Cotton Fabric, XL",
        "Product_cost": 19.99,
        "Product_catagory":"Clothing",
        "Quantity_ available":200
    },
    {
        "Product_id":4,
        "Product_name":"Wireless Earbuds",
        "Product_desc":"Bluetooth, Noise Cancellation",
        "Product_cost": 129.99,
        "Product_catagory":"Electrionics",
        "Quantity_ available":75
    },   
    {
        "Product_id":5,
        "Product_name":"Backpack",
        "Product_desc":"Water Resistant, Laptop Sleeve",
        "Product_cost": 79.99,
        "Product_catagory":"Accessories",
        "Quantity_ available":40
    }
]

@app.route("/products", methods=["GET"])
def get_user():
    return jsonify(data)

if __name__=="__main__":
    app.run(debug=True)