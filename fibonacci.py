#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """

    raise NotImplementedError()


def optimized_fibonacci(f):
    """Calculate fibonacci sequence

    :param int f: index of fth sequence number
    :return int f: value of fth sequence number
    """
    assert isinstance(f, int), f'{f} is not an integer'
    assert f >= 0, f'{f} should be greater than or equal to 0'




class SummableSequence(object):
    def __init__(self, *initial):
        raise NotImplementedError()

    def __call__(self, i):
        raise NotImplementedError()


if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
