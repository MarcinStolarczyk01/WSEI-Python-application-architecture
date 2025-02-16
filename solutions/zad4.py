"""
Napisz program, który oblicza wartości funkcji 𝑓(𝑥) = 𝑐𝑜𝑠(𝑥) + 𝑙𝑛(𝑥 + 1) dla
dużego zestawu wartości 𝑥 (np. od 1 do 1e6 z krokiem 0.01). Podziel zakres 𝑥 na
fragmenty i wykorzystaj moduł multiprocessing, aby równolegle obliczyć wartości
funkcji dla każdego fragmentu.
"""
from concurrent.futures import ProcessPoolExecutor

import numpy as np


f = lambda x: np.cos(x) + np.log(x+1)


if __name__ == "__main__":
    data = np.linspace(1, 1e6, int(1e6*0.1))
    split_arrays = np.array_split(data, 10)
    with ProcessPoolExecutor(max_workers=5) as pool:
        results = pool.map(f, split_arrays)

    for i in results:
        print("piece")
