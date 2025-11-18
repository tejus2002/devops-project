from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello! My DevOps Project is Live.Success! I updated this without touching a terminal!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
