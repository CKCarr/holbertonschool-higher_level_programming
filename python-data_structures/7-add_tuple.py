#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    b = tuple_b + (0, 0)[:2 - len(tuple_b)]
    sum_tuple = (a[0] + b[0], a[1] + b[1])
    return (sum_tuple)
