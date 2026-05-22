from flask import Flask
from app.routes.problems import problems_bp

app = Flask(__name__)

app.register_blueprint(problems_bp)

@app.route("/")
def home():
    return "Dynatrace Microservice is Running"

if __name__ == "__main__":
    app.run(debug=True)