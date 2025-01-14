# Flask AWS and Azure Deployment

This project demonstrates how to deploy a Flask application to both AWS Lambda and Azure Functions.

## Project Structure


- **aws_template.yaml**: AWS SAM template for deploying the Flask app to AWS Lambda.
- **azure_template.json**: Azure Functions template for deploying the Flask app to Azure Functions.
- **deployment/**: Directory containing deployment scripts for AWS and Azure.
  - **aws/**: Directory containing the AWS deployment script.
    - **deploy_aws.sh**: Script to deploy the Flask app to AWS Lambda using AWS SAM CLI.
  - **azure/**: Directory containing the Azure deployment script.
    - **deploy_azure.sh**: Script to deploy the Flask app to Azure Functions using Azure CLI.
- **Dockerfile**: Dockerfile for building a Docker image that includes the Flask app and its dependencies.
- **requirements.txt**: Python dependencies required for the Flask app.
- **src/**: Directory containing the Flask application source code.
  - **app.py**: Main Flask application file.

## Deployment Instructions

### Deploy to AWS Lambda
1- build docker image
docker build docker build -t  datashift-skill-api 

2- docker run image with aws credentials
docker run -d -e AWS_ACCESS_KEY_ID="AKIA3RYC6HZVQ2GBFXFB" -e AWS_SECRET_ACCESS_KEY="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" -e AWS_DEFAULT_REGION="eu-central-1" -p 5000:5000 datashift-skill-api

This will return the cointainer-id:

1. Build the Docker image:
    ```sh
    docker build -t datashift-skill-api .
    ```

2. Run the Docker container with AWS credentials:
    ```sh
    docker run -d -e AWS_ACCESS_KEY_ID="AKIA3RYC6HZVQ2GBFXFB" -e AWS_SECRET_ACCESS_KEY="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" -e AWS_DEFAULT_REGION="eu-central-1" -p 5000:5000 datashift-skill-api
    ```

    This will return the container ID.

3. Enter the container shell using:
    ```sh
    docker exec -it <container-id> /bin/bash
    ```

4. Navigate to the deployment file:
    ```sh
    cd /deployment/aws
    ```

5. Execute the deployment script:
    ```sh
    ./deploy_aws.sh
    

## Flask Application Example Endpoints Provided

- **GET /welcome**: Returns a welcome message with status=200.
- **GET /goodbye**: Returns a goodbye message status=200.