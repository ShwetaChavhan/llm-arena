import logging

def configure_logging():
    """ Configure application-wide logging.
        Log messages to app.log with date, severity level, logger name and messages.
    """
    logging.basicConfig(
        filename='app.log',
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        format=(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        )        
    )
    logging.getLogger(__name__).info("Logging configured.")