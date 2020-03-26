import logging

from unrealmath.addition import add
from unrealmath.subtraction import reduce
from unrealmath import LOGGING_CONFIG

if __name__ == "__main__":
    logging.config.dictConfig(LOGGING_CONFIG)

    add(2, 3)
    reduce(5, 3)
