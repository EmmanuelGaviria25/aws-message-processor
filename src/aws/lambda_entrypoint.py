import json
from src.aws.sqs_handler import receive_messages, delete_message
from src.aws.s3_handler import upload_to_s3
from src.database.mongodb_connector import insert_to_mongo

# Configuración (puedes reemplazar esto por variables de entorno)
SQS_QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/123456789012/my-queue"
S3_BUCKET_NAME = "my-s3-bucket"

def lambda_handler(event, context):
    """
    Función Lambda para procesar mensajes de SQS y guardarlos en MongoDB y S3.
    """
    try:
        messages = receive_messages(SQS_QUEUE_URL)

        for message in messages:
            body = json.loads(message["Body"])
            print(f"Procesando mensaje: {body}")

            # Guardar en MongoDB
            insert_to_mongo(body)

            # Condición para guardar en S3
            if "save_to_s3" in body and body["save_to_s3"]:
                key = f"messages/{body['id']}.json"
                upload_to_s3(S3_BUCKET_NAME, key, body)

            # Eliminar mensaje de la cola
            delete_message(SQS_QUEUE_URL, message["ReceiptHandle"])

        return {"statusCode": 200, "body": "Mensajes procesados correctamente"}
    except Exception as e:
        print(f"Error en lambda_handler: {e}")
        return {"statusCode": 500, "body": str(e)}
