import sys
from silters.analyzer.director import Director
from silters.analyzer.analyzer import FilterAnalyzer, AnnotateAnalyzer


def main(option, path):
    print(option)
    print(path)
    # option = ['annotate', 'storage/text.txt']
    director = Director()
    if 'filter' in option:
        analyzer = FilterAnalyzer()
    elif 'annotate' in option:
        analyzer = AnnotateAnalyzer()
    else:
        print('please specify filter or annotate option ')
    if analyzer:
        # path = option[1]
        try:
            with open(path, 'r') as file:
                pass
                director.analyzer = analyzer
                director.analyze(file)
        except FileNotFoundError as error:
            print(f"Exception: {error}")


main(sys.argv[1], sys.argv[2])
