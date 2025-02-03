from src.aws.sqs_handler import receive_messages, delete_message
from src.aws.s3_handler import upload_to_s3
from src.database.mongodb_connector import insert_to_mongo
from src.config.settings import SQS_QUEUE_URL, S3_BUCKET_NAME
import logging

logger = logging.getLogger(__name__)

def process_sqs_messages():
    """
    Procesa mensajes desde SQS, los guarda en MongoDB, y sube ciertos datos a S3.
    """
    try:
        messages = receive_messages(SQS_QUEUE_URL)

        for message in messages:
            body = message.get("Body")
            if not body:
                logger.warning("Mensaje vacío recibido.")
                continue

            logger.info(f"Procesando mensaje: {body}")

            # Guardar en MongoDB
            data = eval(body)  # Asegúrate de que el body sea un JSON válido
            insert_to_mongo(data)

            # Subir a S3 si aplica
            if "save_to_s3" in data and data["save_to_s3"]:
                key = f"messages/{data['id']}.json"
                upload_to_s3(S3_BUCKET_NAME, key, data)

            # Eliminar mensaje de la cola
            delete_message(SQS_QUEUE_URL, message["ReceiptHandle"])

        logger.info("Todos los mensajes han sido procesados correctamente.")
    except Exception as e:
        logger.error(f"Error procesando mensajes de SQS: {e}")
        raise
