import logging
import time
import functools
import datetime


def decorator1(func):
    def say_hello():
        print("Entry from the decorator 1")
        func()
        print("Exit from the decorator 1")

    return say_hello


def decorator2(func):
    def say_hello():
        print("Entry from the decorator 2")
        func()
        print("Exit from the decorator 2")

    return say_hello


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        logging.info(
            f"""
        Execution time for {func.__name__} execution time: {(time.time() - start):.5f} seconds"""
        )

    return wrapper


def decorator_power_arg(power: int):
    def decorator_power(func):
        def to_power(*args, **kwargs):
            arguments = [arg for arg in args] + [kwarg for kwarg in kwargs.values()]
            arguments = [arg**power for arg in arguments]
            func(*arguments)

        return to_power

    return decorator_power


# todo: Task 1
def list_len(func):
    def count_if_list(*args, **kwargs):
        arguments = [arg for arg in args] + [kwarg for kwarg in kwargs]
        for arg in arguments:
            if isinstance(arg, list):
                print(f"Found list in arguments, it's length is: {len(arg)}")
        func(*args, **kwargs)

    return count_if_list


# todo: Task 2
def log_time(filename: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)

            exec_time = time.time() - start

            logging.basicConfig(
                level="INFO",
                format="%(asctime)s %(name)s %(levelname)s %(message)s",
                filename=filename,
                filemode="a",
                datefmt="%D : %H:%M:%S",
            )
            logger = logging.getLogger()
            logger.info(f"Function {func.__name__} exec time: {exec_time:.7f}")

        return wrapper

    return decorator


# @list_len
@log_time(filename="decorators.log")
def mock_func(a: list, b: list, c=None, d=None, e=None):
    print("mock func doing sth...")


# @decorator1
# @decorator2
@timer
@decorator_power_arg(3)
def summing(a, b):
    print(f"summing: {a, b} = {a + b}")


def main():
    mock_func([1, 2, 3], [], [111], e=0)


if __name__ == "__main__":
    main()
