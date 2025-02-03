from src.utils.logger import setup_logger
import logging

def test_setup_logger():
    logger = setup_logger("TestLogger", logging.DEBUG)
    assert logger.name == "TestLogger"
    assert logger.level == logging.DEBUG
