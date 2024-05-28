import logging
from rich.logging import RichHandler

logging.basicConfig(level="INFO", handlers=[RichHandler()])
logger = logging.getLogger("rich")
