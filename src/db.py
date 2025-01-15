# Initialize the SSM client to fetch the password
import psycopg2
import os
import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ssm = boto3.client("ssm")
DB_HOST = "host"  # Replace with your DB endpoint
DB_USER = "user"  # Replace with your DB user
DB_NAME = "postgres"
DB_PORT = 5432


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
    db_password = get_db_password()  # Fetch the password securely

    if not db_password:
        logger.info("Error: Database password not found.")
        return None

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=db_password,
            dbname=DB_NAME,
            port=DB_PORT,
        )
        logger.info("Successfully connected to the database.")
        return conn
    except Exception as e:
        logger.info(f"Error connecting to the database: {str(e)}")
        return None
