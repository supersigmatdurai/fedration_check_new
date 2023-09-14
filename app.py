from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route and a function to handle requests to that route
@app.route("/")
def hello_world():
    return "Hello, World!"

# Run the app if this script is executed
if __name__ == "__main__":
    app.run()
