#!/bin/bash

# Constants
TEMPLATE_FILE="/app/aws_template.yaml"

# Functions
error_exit() {
  echo "Error: $1" >&2
  exit 1
}

# Check for AWS SAM CLI
if ! command -v sam &>/dev/null; then
  error_exit "AWS SAM CLI is not installed. Please install it and try again."
fi

# Check if template file exists
if [ ! -f "$TEMPLATE_FILE" ]; then
  error_exit "Template file '$TEMPLATE_FILE' not found."
fi

# Build the app
echo "Building the Flask app..."
if ! sam build --template-file "$TEMPLATE_FILE"; then
  error_exit "Build failed. Please check your template and try again."
fi

# Deploy the app to AWS
echo "Deploying the Flask app to AWS Lambda..."
if ! sam deploy --guided --capabilities CAPABILITY_IAM; then
  error_exit "Deployment failed. Please check the AWS SAM logs for details."
fi

echo "Flask app deployed to AWS Lambda successfully!"

