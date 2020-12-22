def add(*args):  # type - tuple
    sum = 0
    for n in args:
        sum += n
    print(sum)


add(1, 3, 5, 6, 7)


def calculate(n, **kwargs):  # type - dictionary
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


