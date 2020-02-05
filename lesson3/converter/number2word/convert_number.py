import inflect


def convert_str2number(input_data):
    if input_data.isdigit():
        return int(input_data)
    else:
        return float(input_data)


def convert(input_data):
    p = inflect.engine()
    numb = convert_str2number(input_data)
    print('number: ', p.number_to_words(numb))

