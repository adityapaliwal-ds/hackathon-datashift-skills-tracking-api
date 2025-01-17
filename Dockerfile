FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    awscli \
    sudo \
    lsb-release \
    gnupg \
    curl \
    unzip \
    libpq-dev \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install AWS SAM CLI
RUN curl -sL https://github.com/aws/aws-sam-cli/releases/download/v1.132.0/aws-sam-cli-linux-arm64.zip -o /tmp/aws-sam-cli.zip \
    && unzip /tmp/aws-sam-cli.zip -d /tmp \
    && sudo ./tmp/install \
    && rm -rf /tmp/aws-sam-cli.zip /tmp/install

# Update install 'less' utility tool used by aws cli
RUN apt-get update && apt-get install -y --no-install-recommends less

# Set the working directory in the container
WORKDIR /app

# Copy the application code and templates to the container
COPY src/ /app
COPY aws-template.yaml /app
COPY deployment/ /app/deployment
COPY requirements.txt /app/requirements.txt

# Make the deploy_aws.sh script executable
RUN chmod +x /app/deployment/aws/deploy_aws.sh

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app (though Lambda will be invoked by API Gateway)
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]