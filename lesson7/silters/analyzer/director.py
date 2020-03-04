from silters.analyzer.analyzer import Analyzer


class Director:
    def __init__(self) -> None:
        self._analyzer = None

    @property
    def analyzer(self) -> Analyzer:
        return self._analyzer

    @analyzer.setter
    def analyzer(self, analyzer: Analyzer) -> None:
        self._analyzer = analyzer

    def analyze(self, file) -> None:
        self.analyzer.analyze(file)

