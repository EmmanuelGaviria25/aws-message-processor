import logging

def setup_logger(name="AWSMessageProcessor", log_level=logging.INFO):
    """
    Configura un logger para el proyecto.
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Formato de los mensajes
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Archivo de logs
    file_handler = logging.FileHandler("logs/project.log")
    file_handler.setFormatter(formatter)

    # Agregar handlers al logger
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
