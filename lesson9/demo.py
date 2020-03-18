import logging

from unrealmath.addition import add
from unrealmath.subtraction import reduce

if __name__ == "__main__":
    logger = logging.getLogger("unrealmath")
    logger.setLevel(logging.INFO)

    add(2, 3)
    reduce(5, 3)
