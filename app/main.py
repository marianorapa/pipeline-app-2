from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! This is an update!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
