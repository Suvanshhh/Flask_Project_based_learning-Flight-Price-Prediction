from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Home page!</h1>"


@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hey {name.title()}, welcome to our Webpage!</h1>"
# We are not hard coding the page with pre defined names as we are taking input from the user dynamically and then url is been created.

if __name__ == "__main__":
    app.run(debug=True)