import os
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env (si existe)
load_dotenv()

# AWS Configuración
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL", "https://sqs.us-east-1.amazonaws.com/123456789012/my-queue")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "my-s3-bucket")

# MongoDB Configuración
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://user:password@cluster.mongodb.net/message_db")

# SQL Server Configuración
SQL_SERVER = os.getenv("SQL_SERVER", "your_sql_server_url")
DATABASE = os.getenv("DATABASE", "your_database_name")
USERNAME = os.getenv("USERNAME", "your_username")
PASSWORD = os.getenv("PASSWORD", "your_password")
