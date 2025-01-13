#!/bin/bash

# Check if AWS SAM CLI is installed
if ! [ -x "$(command -v sam)" ]; then
  echo "Error: AWS SAM CLI is not installed." >&2
  exit 1
fi

# Build the app
sam build

# Deploy the app to AWS
sam deploy --no-confirm-changeset --capabilities CAPABILITY_IAM

echo "Flask app deployed to AWS Lambda successfully!"
