from silters.analyzer.analyzer import Analyzer


class Context:
    def __init__(self, analyzer: Analyzer) -> None:
        self._analyzer = analyzer

    @property
    def analyzer(self) -> Analyzer:
        return self._analyzer

    @analyzer.setter
    def analyzer(self, analyzer: Analyzer) -> None:
        self._analyzer = analyzer

    def analyze(self, file) -> None:
        self.analyzer.analyze(file)

