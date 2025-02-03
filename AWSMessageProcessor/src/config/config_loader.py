import logging
from src.config.settings import *

logger = logging.getLogger(__name__)

def load_config():
    """
    Carga y valida la configuración del proyecto.
    """
    config = {
        "AWS_REGION": AWS_REGION,
        "SQS_QUEUE_URL": SQS_QUEUE_URL,
        "S3_BUCKET_NAME": S3_BUCKET_NAME,
        "MONGO_URI": MONGO_URI,
        "SQL_SERVER": SQL_SERVER,
        "DATABASE": DATABASE,
        "USERNAME": USERNAME,
        "PASSWORD": PASSWORD,
    }
    
    # Log de configuración cargada
    logger.info("Configuraciones cargadas correctamente.")
    return config
