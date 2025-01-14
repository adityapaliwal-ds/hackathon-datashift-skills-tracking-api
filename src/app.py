from flask import Flask, jsonify
import awsgi

app = Flask(__name__)


@app.route("/welcome")
def index():
    return jsonify(
        status=200, message="Welcome to datashift data engineering hackathon"
    )


@app.route("/goodbye")
def goodbye():
    return jsonify(
        status=200, message="Goodbye from datashift data engineering hackathon"
    )


# Lambda handler
def lambda_handler(event, context):
    return awsgi.response(app, event, context)


if __name__ == "__main__":
    app.run(debug=True)
