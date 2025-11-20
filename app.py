from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <style>
        body {
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: sans-serif;
            background-color: #f0f2f5;
        }
        h1 {
            color: #333;
            font-size: 3rem;
        }
    </style>
    
    <h1>Hello!!My DevOps Project</h1>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
