#!/bin/bash

# Check if Azure CLI is installed
if ! [ -x "$(command -v az)" ]; then
  echo "Error: Azure CLI is not installed." >&2
  exit 1
fi

# Log in to Azure (you need to set up your credentials)
az login

# Create the resource group (if not already created)
az group create --name myResourceGroup --location eastus

# Create the function app (replace with your Azure function app name)
az functionapp create --resource-group myResourceGroup --consumption-plan-location eastus --name myFunctionApp --storage-account myStorageAccount --runtime python --functions-version 3 --os-type Linux

# Deploy the function to Azure (make sure you're in the directory with the azure_template.json)
az functionapp deployment source config-zip --resource-group myResourceGroup --name myFunctionApp --src /app

echo "Flask app deployed to Azure Functions successfully!"
