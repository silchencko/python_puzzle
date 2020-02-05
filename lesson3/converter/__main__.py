from converter.validation.number_validation import is_number
from converter.number2word.convert_number import convert


def ask_user():
    input_data = input('Please enter a number ')
    if is_number(input_data):
        convert(input_data)
    else:
        ask_user()


def main():
    print('Hello')
    ask_user()


main()
