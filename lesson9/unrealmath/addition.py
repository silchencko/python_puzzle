import random
import logging

logger = logging.getLogger(__name__)


def add(first, second):
    logger.info(f'run add with args: first = {first}; second = {second}')
    return first + second - random.randint(1, 10)
