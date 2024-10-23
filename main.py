def decorator1(func):
    def say_hello():
        print('Entry from the decorator 1')
        func()
        print('Exit from the decorator 1')
    return say_hello


def decorator2(func):
    def say_hello():
        print('Entry from the decorator 2')
        func()
        print('Exit from the decorator 2')


    return say_hello


@decorator1
@decorator2
def summing():
    print('summing!')


def main():
    summing()


if __name__ == '__main__':
    main()
