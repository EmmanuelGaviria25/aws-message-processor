import os
import json
import logging

logger = logging.getLogger(__name__)

def validate_json_file(file_path):
    """
    Valida si un archivo contiene JSON válido.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info(f"Archivo JSON válido: {file_path}")
            return data
    except json.JSONDecodeError:
        logger.error(f"Archivo JSON inválido: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error leyendo el archivo {file_path}: {e}")
        raise

def read_json_files(input_folder):
    """
    Lee y valida todos los archivos JSON en una carpeta.
    """
    try:
        files = [
            os.path.join(input_folder, f)
            for f in os.listdir(input_folder)
            if f.endswith(".json")
        ]
        logger.info(f"{len(files)} archivos JSON encontrados en {input_folder}.")
        all_data = []
        for file_path in files:
            try:
                data = validate_json_file(file_path)
                all_data.append(data)
            except Exception as e:
                logger.error(f"Error procesando el archivo {file_path}: {e}")
        return all_data
    except Exception as e:
        logger.error(f"Error leyendo la carpeta {input_folder}: {e}")
        raise
