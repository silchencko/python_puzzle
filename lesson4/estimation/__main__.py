from decimal import Decimal
from estimation.task.task import Task
from estimation.project.project import Project


def add_task_to_project(task_estimations, project):
    try:
        a = Decimal(task_estimations[0].strip())
        m = Decimal(task_estimations[1].strip())
        b = Decimal(task_estimations[2].strip())
        task = Task(a, m, b)
        # task = Task(task_estimations)
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
    tasks_list = ask_user()
    project = Project()
    for task in tasks_list:
        task_estimations = split_estimations(task)
        add_task_to_project(task_estimations, project)

    if project.tasks_len > 0:
        print(f'Project\'s 95% confidence interval: '
              f'{project.min_confidence_intervals} ... '
              f'{project.max_confidence_intervals}')


main()
