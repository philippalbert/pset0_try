#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """

    raise int(str(some_int[-8:]))


def optimized_fibonacci(f):
    """Calculate fibonacci sequence

    :param int f: index of fth sequence number
    :return int f: value of fth sequence number
    """
    assert isinstance(f, int), f"{f} is not an integer"
    assert f >= 0, f"{f} should be greater than or equal to 0"

    # in case f is smaller 2 we just return f
    if f < 2:
        return f

    # create start variables
    s1, s2 = 0, 1
    for i in range(2, f):

        s1, s2 = s2, s1 + s2

    return s1 + s2


class SummableSequence(object):
    def __init__(self, *initial):
        raise NotImplementedError()

    def __call__(self, i):
        raise NotImplementedError()


if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
