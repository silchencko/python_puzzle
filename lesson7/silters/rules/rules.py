from silters.rules.filter import Filter


def count_letter_appearance(line, let):
    return len(list(filter(lambda letter: letter == let, line)))


class RuleFP001(Filter):
    def name(self):
        return 'FP001'

    def matches(self, line: str):
        return line.endswith('.')


class RuleFP002(Filter):
    def name(self):
        return 'FP002'

    def matches(self, line: str):
        return len(line) < 100 and line != '\n'


class RuleFP003(Filter):
    def name(self):
        return 'FP003'

    def matches(self, line: str):
        return count_letter_appearance(line, 'a') >= 5


class RuleFN201(Filter):
    def name(self):
        return 'FN201'

    def matches(self, line: str):
        return count_letter_appearance(line, 'z') >= 3


class RuleFN202(Filter):
    def name(self):
        return 'FN202'

    def matches(self, line: str):
        return line == '\n'


class RuleFN203(Filter):
    def name(self):
        return 'FN203'

    def matches(self, line: str):
        return any(char.isalpha() for char in line)


rule_FP001 = RuleFP001()
rule_FP002 = RuleFP002()
rule_FP003 = RuleFP003()
rule_FN201 = RuleFN201()
rule_FN202 = RuleFN202()
rule_FN203 = RuleFN203()
