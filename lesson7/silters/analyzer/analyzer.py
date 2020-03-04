from abc import ABC, abstractmethod
from silters.rules.rules import *


class Analyzer(ABC):
    @abstractmethod
    def analyze(self, file):
        pass

    @abstractmethod
    def check_rule_fp001(self):
        pass

    @abstractmethod
    def check_rule_fp002(self):
        pass

    @abstractmethod
    def check_rule_fp003(self):
        pass

    @abstractmethod
    def check_rule_fn201(self):
        pass

    @abstractmethod
    def check_rule_fn202(self):
        pass

    @abstractmethod
    def check_rule_fn203(self):
        pass


class FilterAnalyzer(Analyzer):
    def analyze(self, file):
        for i, line in enumerate(file):
            if self.check_rule_fp001(line) or self.check_rule_fp002(line) or self.check_rule_fp003(line):
                print(line)

    def check_rule_fp001(self, line):
        return rule_FP001.matches(line)

    def check_rule_fp002(self, line):
        return rule_FP002.matches(line)

    def check_rule_fp003(self, line):
        return rule_FP003.matches(line)

    def check_rule_fn201(self, line):
        return rule_FN201.matches(line)

    def check_rule_fn202(self, line):
        return rule_FN202.matches(line)

    def check_rule_fn203(self, line):
        return rule_FN203.matches(line)


class AnnotateAnalyzer(Analyzer):
    def analyze(self, file):
        for i, line in enumerate(file):
            result = ''
            fp001_result = self.check_rule_fp001(line)
            fp002_result = self.check_rule_fp002(line)
            fp003_result = self.check_rule_fp003(line)
            fn201_result = self.check_rule_fn201(line)
            fn202_result = self.check_rule_fn202(line)
            fn203_result = self.check_rule_fn203(line)
            if fp001_result:
                result += fp001_result + ' '
            if fp002_result:
                result += fp002_result + ' '
            if fp003_result:
                result += fp003_result + ' '
            if fn201_result:
                result += fn201_result + ' '
            if fn202_result:
                result += fn202_result + ' '
            if fn203_result:
                result += fn203_result + ' '
            if len(result) > 0:
                print(i + 1, ': ', result)

    def check_rule_fp001(self, line):
        if rule_FP001.matches(line):
            return rule_FP001.name()

    def check_rule_fp002(self, line):
        if rule_FP002.matches(line):
            return rule_FP002.name()

    def check_rule_fp003(self, line):
        if rule_FP003.matches(line):
            return rule_FP003.name()

    def check_rule_fn201(self, line):
        if rule_FN201.matches(line):
            return rule_FN201.name()

    def check_rule_fn202(self, line):
        if rule_FN202.matches(line):
            return rule_FN202.name()

    def check_rule_fn203(self, line):
        if rule_FN203.matches(line):
            return rule_FN203.name()
