import datetime
import os
import logging


# Record logs into 'logger.log' file
logging.basicConfig(filename='logger.log', filemode='w', level=logging.INFO)


# Context manager
# logs file execution time
class TemporaryFile:
    def __init__(self, name, mode):
        self.file = open(name, mode)

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.execution_time = datetime.datetime.now() - self.start_time
        self.file.close()
        logging.info(f'Execution time: %s  {self.execution_time}', self.file)


def run_quiz_section(file_name, answer_file):
    with TemporaryFile(file_name, 'r') as quiz_section:
        lines = quiz_section.readlines()
        for line in lines:
            question = line.strip()
            answer = input(f'{question} - ')
            answer_file.write(f'{question}: {answer}\n')


def run_quiz(path, answers_storage):
    sections = os.listdir(path)
    for section in sections:
        file_name = os.path.join(path, section)
        run_quiz_section(file_name, answers_storage)


# Record answers into 'answers.txt' file
def main():
    quiz_path = 'quiz'
    with TemporaryFile('answers.txt', 'w') as answers:
        if os.path.exists(quiz_path):
            run_quiz(quiz_path, answers)


# main block
if __name__ == '__main__':
    main()
