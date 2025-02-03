import pymongo
import logging
from src.config.settings import MONGO_URI

logger = logging.getLogger(__name__)

# Conexión global a MongoDB
mongo_client = pymongo.MongoClient(MONGO_URI)
db = mongo_client.get_database("message_db")  # Nombre de la base de datos
collection = db.get_collection("messages")   # Nombre de la colección

def insert_to_mongo(data):
    """
    Inserta un documento en la colección MongoDB.
    """
    try:
        result = collection.insert_one(data)
        logger.info(f"Documento insertado con ID: {result.inserted_id}")
        return result.inserted_id
    except Exception as e:
        logger.error(f"Error insertando en MongoDB: {e}")
        raise

def fetch_all_documents():
    """
    Obtiene todos los documentos de la colección MongoDB.
    """
    try:
        documents = list(collection.find())
        logger.info(f"{len(documents)} documentos recuperados de MongoDB.")
        return documents
    except Exception as e:
        logger.error(f"Error obteniendo documentos de MongoDB: {e}")
        raise
