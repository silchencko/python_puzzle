def find_pair(number, numbers):
    for pair in numbers:
        if int(number) + int(pair) == 10:
            print(number + ' + ' + pair)


def main(parameters):
    index = 0
    for number in parameters:
        if index < len(parameters) - 1:
            find_pair(number, parameters[index + 1:])
        index += 1


# main block
if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
