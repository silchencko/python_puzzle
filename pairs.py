def find_pair(number, numbers):
    for pair in numbers:
        if int(number) + int(pair) == 10:
            return number + " + " + pair


def main(parameters):
    params = sorted(parameters)
    pairs_set = set()
    for index, number in enumerate(params):
        if index < len(params) - 1:
            pair = find_pair(number, params[index + 1:])
            if (pair):
                pairs_set.add(pair)
    print(pairs_set)


# main block
if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
