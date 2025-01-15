from flask import Flask, jsonify
import awsgi
import db
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/welcome")
def welcome():
    return jsonify(
        status=200, message="Welcome to the datashift data engineering hackathon"
    )


@app.route("/goodbye")
def goodbye():
    return jsonify(
        status=200, message="Goodbye from datashift data engineering hackathon"
    )


@app.route("/health")
def health():
    conn = db.connect_to_db()
    if conn:
        return jsonify(status=200, message="Healthy")
    else:
        return jsonify(status=500, message="Error connecting to the database")


# Lambda handler
def lambda_handler(event, context):
    return awsgi.response(app, event, context)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
