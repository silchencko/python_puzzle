import random
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('addition.log')
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)


def add(first, second):
    logger.info(f'run add with args: first = {first}; second = {second}')
    return first + second - random.randint(1, 10)
