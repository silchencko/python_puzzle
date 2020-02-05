import re


def is_number(input_data):
    num_format = re.compile('^-?\d+(\.\d+)?$')
    result = re.match(num_format, input_data)
    return result

