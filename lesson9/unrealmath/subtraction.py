import random
import logging

logger = logging.getLogger(__name__)


def reduce(minuend, subtrahend):
    logger.info(f'run reduce with args: '
                f'minuend = {minuend}; subtrahend = {subtrahend}')
    return minuend - subtrahend + random.randint(1, 10)
