# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route("/")
def index():
    return "Hello world"


@app.route("/test")
def test():
    return "This is a testpage"


@app.route("/123")
def numbers():
    return "123 roger 123"

if __name__ == "__main__":
    app.run()