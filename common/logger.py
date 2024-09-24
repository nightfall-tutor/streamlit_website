from common.path_handler import path_handler
import logging
import sys


default_format = "%(asctime)s [%(levelname)s] %(filename)s (line:%(lineno)d) %(message)s"

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(logging.Formatter(default_format))
console_handler.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(path_handler.log_file_path, mode='a', encoding='utf8')
file_handler.setFormatter(logging.Formatter(default_format))
file_handler.setLevel(logging.DEBUG)

logger = logging.Logger(name="logger", level=logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.debug("Initialize logger")

