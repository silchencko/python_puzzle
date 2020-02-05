def is_empty_line(line):
    return line == '\n'


def count_z(line):
    return len(list(filter(lambda letter: letter == 'z', line)))


def analyze(file):
    empty_lines = 0
    lines_with_z = 0
    z_count = 0
    lines_with_and = 0

    for i, line in enumerate(file):
        if is_empty_line(line):
            empty_lines += 1
        if 'z' in line:
            lines_with_z += 1
            z_count += count_z(line)
        if 'and' in line:
            lines_with_and += 1

    print(' total lines: ', i + 1)
    print(' empty lines: ', empty_lines)
    print(' lines with "z": ', lines_with_z)
    print(' "z" count: ', z_count)
    print(' lines with "and": ', lines_with_and)


def ask_user():
    path = input(f'Please provide a path to the file you want to analyze '
                 + f'(enter "no" to quit): ')
    if path != 'no':
        print('File: ', path)
        with open(path, 'r') as file:
            analyze(file)
            ask_user()


def main():
    ask_user()


# main block
if __name__ == '__main__':
    main()
