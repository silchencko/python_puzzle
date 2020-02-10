from estimation.task.task import Task
from estimation.project.project import Project
from decimal import Decimal


def add_task_to_project(task_estomations, project):
    try:
        task = Task(Decimal(task_estomations[0].strip()),
                    Decimal(task_estomations[1].strip()),
                    Decimal(task_estomations[2].strip()))
        project.add_task(task)
    except:
        print('Estimations must be numbers')


def split_estimations(user_input):
    estimations = user_input.split(', ')
    if len(estimations) == 3:
        return estimations
    else:
        print('Each task has to have 3 estimations')


def split_tasks(user_input):
    tasks = user_input.split(';')
    if len(tasks) > 0:
        return tasks
    else:
        print('Enter estimation for at list one task')


def ask_user():
    tasks_input = input('Please, enter tasks estimations. ' +
                        'For each task enter 3 numbers: ' +
                        'the best-case estimate, the most likely estimate ' +
                        'and the worst-case estimate.' +
                        'Split up estimates with coma and space. ' +
                        'Split up tasks with semicolons ')
    return split_tasks(tasks_input)


def main():
    try:
        tasks_list = ask_user()
        project = Project()
        for task in tasks_list:
            task_estimations = split_estimations(task)
            add_task_to_project(task_estimations, project)

        print(f'Project\'s 95% confidence interval: '
              f'{project.calculate_min_confidence_intervals()} ... '
              f'{project.calculate_max_confidence_intervals()}')
    except:
        pass


main()
