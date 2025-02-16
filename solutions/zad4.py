"""
Napisz program, który oblicza wartości funkcji 𝑓(𝑥) = 𝑐𝑜𝑠(𝑥) + 𝑙𝑛(𝑥 + 1) dla
dużego zestawu wartości 𝑥 (np. od 1 do 1e6 z krokiem 0.01). Podziel zakres 𝑥 na
fragmenty i wykorzystaj moduł multiprocessing, aby równolegle obliczyć wartości
funkcji dla każdego fragmentu.
"""

from concurrent.futures import ProcessPoolExecutor
from time import time
import numpy as np


def transform(array: np.ndarray) -> np.ndarray:
    f = lambda x: np.asarray([np.cos(num) + np.log(num + 1) for num in x])
    return f(array)


if __name__ == "__main__":

    data = np.linspace(1, 1e6, int(1e6 / 0.1))
    split_arrays = np.array_split(data, 10)

    # <no splitting>
    start = time()
    results = transform(data)
    print("Exec time without splitting: ", time() - start)
    # </no splitting>

    del results
    # <splitting>
    start = time()
    with ProcessPoolExecutor(max_workers=10) as pool:
        results = pool.map(transform, split_arrays)
    print("Exec time with 10 workers: ", time() - start)
    results = np.concatenate([r for r in results])
    # </splitting>
