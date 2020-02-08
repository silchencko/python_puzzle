import inflect
from decimal import Decimal


def convert_str2number(input_data):
    return Decimal(input_data)


def convert(input_data):
    p = inflect.engine()
    numb = convert_str2number(input_data)
    print('number: ', p.number_to_words(numb))
