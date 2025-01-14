#!/bin/bash

# Check if AWS SAM CLI is installed
if ! [ -x "$(command -v sam)" ]; then
  echo "Error: AWS SAM CLI is not installed." >&2
  exit 1
fi

# Build the app
sam build --template-file /app/aws_template.yaml

# Deploy the app to AWS
sam deploy --guided --capabilities CAPABILITY_IAM

echo "Flask app deployed to AWS Lambda successfully!"
