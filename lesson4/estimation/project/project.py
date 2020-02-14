from math import sqrt
from estimation.task.task import Task


class Project:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)

    @property
    def tasks_len(self):
        return len(self.tasks)

    @property
    def estimate(self):
        estimate = 0
        for task in self.tasks:
            estimate += task.estimate
        return estimate

    @property
    def standard_deviation(self):
        sd = 0
        for task in self.tasks:
            sd += task.standard_deviation ** 2
        return round(sqrt(sd))

    @property
    def max_confidence_intervals(self):
        return round(self.estimate +
                     2 * self.standard_deviation)

    @property
    def min_confidence_intervals(self):
        return round(self.estimate -
                     2 * self.standard_deviation)
