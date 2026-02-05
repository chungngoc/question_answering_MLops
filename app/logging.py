import logging
import sys

def get_logger(name: str) -> logging.Logger:
    """
    Get a logger with the specified name.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: A configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create console handler and set level to debug
    handler = logging.StreamHandler(sys.stdout)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add formatter to handler
    handler.setFormatter(formatter)

    # Add handler to logger
    if not logger.handlers:
        logger.addHandler(handler)

    return logger