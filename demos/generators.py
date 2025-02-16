# todo: task 4
class Collatza:
    def __init__(self, prev: int):
        if prev <= 0:
            raise ValueError
        self._prev = prev

    def __iter__(self):
        return self

    def __next__(self):
        if self._prev == 1:
            raise StopIteration
        if abs(self._prev % 2):
            current = 3*self._prev + 1
        else:
            current = round(self._prev /2)

        self._prev = current
        return current

def main():
    for num in Collatza(6):
        print(num)

if __name__ == '__main__':
    main()
