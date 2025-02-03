import argparse
from src.services.message_processor import process_sqs_messages
from src.services.downloader_service import download_urls
from src.utils.logger import setup_logger

# Configurar el logger global
logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="AWS Message Processor CLI")
    
    # Comandos disponibles
    parser.add_argument(
        "command",
        choices=["process_sqs", "download_urls"],
        help="Comando a ejecutar: 'process_sqs' para procesar mensajes de SQS o 'download_urls' para descargar archivos concurrentemente"
    )
    
    args = parser.parse_args()

    # Ejecutar según el comando proporcionado
    if args.command == "process_sqs":
        logger.info("Iniciando procesamiento de mensajes desde SQS...")
        process_sqs_messages()
        logger.info("Procesamiento de mensajes desde SQS completado.")
    elif args.command == "download_urls":
        logger.info("Iniciando descarga de URLs...")
        download_urls()
        logger.info("Descarga de URLs completada.")

if __name__ == "__main__":
    main()
