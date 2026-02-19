import psycopg2
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="Productsdb",
    user="postgres",
    password="pb10cp3612",
    port=5432
)

cursor = conn.cursor()
@app.route("/")
def login_page():
    return render_template("Product_login.html")

@app.route("/catalouge")
def catalogue():
    return render_template("Product_catalouge.html")

@app.route("/products", methods=["GET"])
def get_products():
    cursor.execute("SELECT * FROM products ORDER BY product_id;")
    rows = cursor.fetchall()

    products = []
    for row in rows:
        products.append({
            "product_id": row[0],
            "product_name": row[1],
            "product_desc": row[2],
            "product_cost": float(row[3]),
            "product_category": row[4],
            "quantity_available": row[5]
        })

    return jsonify(products)

@app.route("/products", methods=["POST"])
def add_product():
    data = request.json

    cursor.execute("""
        INSERT INTO products
        (product_name, product_desc, product_cost, product_category, quantity_available)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING product_id;
    """, (
        data["product_name"],
        data["product_desc"],
        float(data["product_cost"]),
        data["product_category"],
        int(data["quantity_available"])
    ))

    new_id = cursor.fetchone()[0]
    conn.commit()

    return jsonify({
        "message": "Product added successfully!",
        "product_id": new_id
    }), 201


@app.route("/product/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.json

    cursor.execute("""
        UPDATE products
        SET product_name = %s,
            product_desc = %s,
            product_cost = %s,
            product_category = %s,
            quantity_available = %s
        WHERE product_id = %s;
    """, (
        data["product_name"],
        data["product_desc"],
        float(data["product_cost"]),
        data["product_category"],
        int(data["quantity_available"]),
        product_id
    ))

    conn.commit()

    return jsonify({"message": "Product Details updated successfully!"})


@app.route("/product/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    cursor.execute(
        "DELETE FROM products WHERE product_id = %s;",
        (product_id,)
    )
    conn.commit()
    return jsonify({"message": "Product deleted successfully!"})

@app.route("/products/category/<string:category>", methods=["GET"])
def filter_by_category(category):

    cursor.execute(
        "SELECT * FROM products WHERE product_category = %s ORDER BY product_id;",
        (category,)
    )

    rows = cursor.fetchall()

    products = []
    for row in rows:
        products.append({
            "product_id": row[0],
            "product_name": row[1],
            "product_desc": row[2],
            "product_cost": float(row[3]),
            "product_category": row[4],
            "quantity_available": row[5]
        })

    return jsonify(products)
@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.json

        cursor.execute(
            "SELECT * FROM users WHERE user_email = %s;",
            (data["user_email"],)
        )
        existing_user = cursor.fetchone()

        if existing_user:
            return jsonify({
                "message": "Email already exists"
            }), 400

       
        cursor.execute("""
            INSERT INTO users (user_name, user_email, user_password)
            VALUES (%s, %s, %s)
            RETURNING user_id;
        """, (
            data["user_name"],
            data["user_email"],
            data["user_password"]
        ))

        new_id = cursor.fetchone()[0]
        conn.commit()

        return jsonify({
            "message": "User Registered Successfully",
            "user_id": new_id
        }), 201

    except Exception as e:
        conn.rollback() 
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/login", methods=["POST"])
def login():

    data = request.json

    cursor.execute("""
        SELECT * FROM users
        WHERE user_email = %s AND user_password = %s;
    """, (
        data["user_email"],
        data["user_password"]
    ))

    user = cursor.fetchone()

    if user:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)






