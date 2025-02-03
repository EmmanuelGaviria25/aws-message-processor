import boto3
import json
import logging

logger = logging.getLogger(__name__)

# Cliente S3
s3_client = boto3.client("s3", region_name="us-east-1")

def upload_to_s3(bucket_name, key, data):
    """
    Sube un archivo JSON a un bucket S3.
    """
    try:
        s3_client.put_object(
            Bucket=bucket_name, 
            Key=key, 
            Body=json.dumps(data),
            ContentType="application/json"
        )
        logger.info(f"Archivo subido a S3: {bucket_name}/{key}")
    except Exception as e:
        logger.error(f"Error subiendo archivo a S3: {e}")
        raise
