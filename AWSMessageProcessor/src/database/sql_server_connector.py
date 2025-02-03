import pyodbc
import logging
from src.config.settings import SQL_SERVER, DATABASE, USERNAME, PASSWORD

logger = logging.getLogger(__name__)

# Configuración de la conexión
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SQL_SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={USERNAME};"
    f"PWD={PASSWORD};"
)

def get_sql_connection():
    """
    Devuelve una conexión activa a SQL Server.
    """
    try:
        conn = pyodbc.connect(conn_str)
        logger.info("Conexión a SQL Server exitosa.")
        return conn
    except Exception as e:
        logger.error(f"Error conectando a SQL Server: {e}")
        raise

def insert_into_sql_server(table_name, data):
    """
    Inserta un registro en la tabla especificada.
    """
    try:
        conn = get_sql_connection()
        cursor = conn.cursor()
        query = f"""
        INSERT INTO {table_name} (id, name, value, timestamp)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, data["id"], data["name"], data["value"], data["timestamp"])
        conn.commit()
        logger.info(f"Registro insertado en {table_name}: {data}")
    except Exception as e:
        logger.error(f"Error insertando en SQL Server: {e}")
        raise
    finally:
        cursor.close()
        conn.close()
