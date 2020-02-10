class Task:
    def __init__(self, a, m, b):
        self._a = a
        self._m = m
        self._b = b

    def calculate_estimate(self):
        return round((self._a + 4 * self._m + self._b) / 6)

    def calculate_standard_deviation(self):
        return round((self._b - self._a) / 6)
