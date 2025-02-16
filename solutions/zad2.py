"""
Napisz klasę, która będzie implementować generator kolejnych n potęg liczby a.
Użyj metod magicznych __iter__() i __next__(). Liczby n i a powinny być
parametrami wejściowymi generatora.
"""


class PowerGen:
    def __init__(self, a, n: int):
        self._n = n
        self._a = a
        self._current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current > self._n:
            raise StopIteration
        result = self._a**self._current
        self._current += 1
        return result


if __name__ == "__main__":
    gen = PowerGen(2, 3)
    for _ in gen:
        print(_)
