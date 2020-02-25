import functools
import time


def timer(func):
    """Prints the runtime of the decorated function."""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            value = func(*args, **kwargs)
            return value
        except Exception as error:
            raise error
        finally:
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
    return wrapper_timer


@timer
def ask_age():
    answer = input('Your age? ')
    try:
        print(f'Your age is {int(answer)}')
    except ValueError as error:
        print(f"Exception: {error}")


def main():
    ask_age()


# main block
if __name__ == '__main__':
    main()
