"""
Napisz dekorator funkcji, który będzie logował informację o nazwie i typie
wszystkich parametrów wejściowych funkcji dekorowanej w postaci:
{<nazwa_parametru>: <typ_danych>, …}.
"""

from functools import wraps
import logging
import inspect

logging.basicConfig(level="INFO")
logger = logging.getLogger(__file__)


def logg_params(func):
    @wraps(func)
    def log(*args, **kwargs):
        args_names = list(inspect.signature(func).parameters.keys())
        args_names = args_names[: len(args)]
        params = [(name, type(val)) for name, val in zip(args_names, args)] + [
            (name, type(val)) for name, val in kwargs.items()
        ]
        logger.info(f"Parameters passed to function {func.__name__}:")
        for p in params:
            logger.info(f"Parameter: {p[0]}, Type: {p[1]}")
        result = func(*args, **kwargs)
        return result

    return log


@logg_params
def my_func(arg1, arg2, arg3, **kwargs):
    logger.info("Function executed")


if __name__ == "__main__":
    my_func(1, 1.1, "one", kw1=["one", "two"], kw2=("three", "four"))
