from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Lab 4 DevOps: AWS EC2</h1>
    <p>Flask application successfully deployed via Gunicorn on Amazon EC2!</p>
    <p>Student: Denys Riabchun</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)