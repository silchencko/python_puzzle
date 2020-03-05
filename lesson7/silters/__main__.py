import sys
from silters.analyzer.context import Context
from silters.analyzer.analyzer import FilterAnalyzer, AnnotateAnalyzer


"""Run python -m silters filter 'silters/storage/text.txt' or python -m silters annotate 'silters/storage/text.txt' """


def main(option, path):
    if 'filter' in option:
        analyzer = FilterAnalyzer()
    elif 'annotate' in option:
        analyzer = AnnotateAnalyzer()
    else:
        print('please specify filter or annotate option ')

    if analyzer:
        try:
            with open(path, 'r') as file:
                pass
                context = Context(analyzer)
                context.analyze(file)
        except FileNotFoundError as error:
            print(f"Exception: {error}")


main(sys.argv[1], sys.argv[2])
