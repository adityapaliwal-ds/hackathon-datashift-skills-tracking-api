# Initialize the SSM client to fetch the password
import psycopg2
import os
import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ssm = boto3.client("ssm")


def get_db_password():
    """Fetch the DB password securely from SSM"""
    try:
        response = ssm.get_parameter(
            Name="/team1/rds/password",
            WithDecryption=True,  # Decrypt the SecureString parameter
        )
        return response["Parameter"]["Value"]
    except Exception as e:
        logger.info(f"Error fetching DB password: {str(e)}")
        return None


def connect_to_db():
    """Connect to the PostgreSQL database and return the connection object"""
    db_host = "hackathon-test-api-rdsinstance-bvybzxgbfsoj.c38uk6c8utvq.eu-central-1.rds.amazonaws.com"
    db_user = "testuser"
    db_name = "postgres"
    db_password = get_db_password()  # Fetch the password securely

    if not db_password:
        logger.info("Error: Database password not found.")
        return None

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=db_host, user=db_user, password=db_password, dbname=db_name, port=5432
        )
        logger.info("Successfully connected to the database.")
        return conn
    except Exception as e:
        logger.info(f"Error connecting to the database: {str(e)}")
        return None
