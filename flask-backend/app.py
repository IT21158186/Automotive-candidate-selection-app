from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/signup", methods=["POST"])
def signup():

    email = request.json["email"]
    password = request.json["password"]

    return jsonify({
        "id": "1",
        "email": email
    })

if __name__ == "__main__":
    app.run(debug=True)