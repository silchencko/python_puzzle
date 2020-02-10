from math import sqrt
from estimation.task.task import Task


class Project:
    tasks = []

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)

    def calculate_estimate(self):
        estimate = 0
        for task in self.tasks:
            estimate += task.calculate_estimate()
        return estimate

    def calculate_standard_deviation(self):
        sd = 0
        for task in self.tasks:
            sd += task.calculate_standard_deviation() ** 2
        return round(sqrt(sd))

    def calculate_max_confidence_intervals(self):
        return round(self.calculate_estimate() +
                     2 * self.calculate_standard_deviation())

    def calculate_min_confidence_intervals(self):
        return round(self.calculate_estimate() -
                     2 * self.calculate_standard_deviation())
