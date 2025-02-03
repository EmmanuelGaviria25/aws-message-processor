import boto3
import json
import logging

logger = logging.getLogger(__name__)

# Cliente SQS
sqs_client = boto3.client("sqs", region_name="us-east-1")

def receive_messages(queue_url, max_messages=10, wait_time=5):
    """
    Recibe mensajes desde una cola SQS.
    """
    try:
        response = sqs_client.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=max_messages,
            WaitTimeSeconds=wait_time,
        )
        messages = response.get("Messages", [])
        logger.info(f"Recibidos {len(messages)} mensajes desde SQS.")
        return messages
    except Exception as e:
        logger.error(f"Error recibiendo mensajes de SQS: {e}")
        raise

def delete_message(queue_url, receipt_handle):
    """
    Elimina un mensaje procesado de la cola SQS.
    """
    try:
        sqs_client.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
        logger.info("Mensaje eliminado de la cola SQS.")
    except Exception as e:
        logger.error(f"Error eliminando mensaje de SQS: {e}")
        raise
