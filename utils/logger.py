from loguru import logger
import sys


logger.remove()
logger.add(sys.stderr, format="<level>{message}</level>", level="INFO", colorize=True)
logger.add("history.log", rotation="5 MB", format="{time} {level} {message}", level="DEBUG")
logger.debug("Logger initialized")
