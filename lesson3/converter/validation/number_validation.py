from decimal import Decimal


def is_number(input_data):
    try:
        Decimal(input_data)
        return True
    except:
        return False
