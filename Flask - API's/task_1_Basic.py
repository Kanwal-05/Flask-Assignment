
from flask import Flask , jsonify
app=Flask("Project 1")

data={
        "Message":"Hello, World !"
    }

@app.route("/", methods=["GET"])
def get_user():
    return jsonify(data)

if __name__=="__main__":
    app.run(debug=True)