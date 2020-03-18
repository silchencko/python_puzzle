import random
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('subtraction.log')
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)


def reduce(minuend, subtrahend):
    logger.info(f'run reduce with args: '
                f'minuend = {minuend}; subtrahend = {subtrahend}')
    return minuend - subtrahend + random.randint(1, 10)
