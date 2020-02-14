class Task:
    def __init__(self, a, m, b):
        self._a = a
        self._m = m
        self._b = b

    # def __init__(self, estimations):
    #     self._a = Decimal(estimations[0].strip())
    #     self._m = Decimal(estimations[1].strip())
    #     self._b = Decimal(estimations[2].strip())

    @property
    def estimate(self):
        return round((self._a + 4 * self._m + self._b) / 6)

    @property
    def standard_deviation(self):
        return round((self._b - self._a) / 6)
