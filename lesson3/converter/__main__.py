from converter.validation.number_validation import is_number
from converter.number2word.convert_number import convert


def ask_user():
    input_data = input('Please enter a number ')
    while not is_number(input_data):
        input_data = input(f'{input_data}' +
                           f' is not a number. Please enter a number ')

    convert(input_data)


def main():
    print('Hello')
    ask_user()


main()
