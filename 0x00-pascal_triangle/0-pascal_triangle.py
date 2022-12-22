#!/usr/bin/python3
""" A Pascal Triangle Implementation """


def factorial(n):
    if not isinstance(n, int):
        raise TypeError(f"{n} must be an integer")
    if n < 0:
        return False
    if n == 0:
        return 1
    else:
        fact = n * factorial(n-1)
        return fact


def combination(n, r):
    return int(factorial(n)/(factorial(n-r)*factorial(r)))


def pascal_triangle(n):
    if not isinstance(n, int):
        raise TypeError(f"{n} must be an integer")
        return False
    # if n <= 0:
    #     raise ValueError("n cannot be less than 0")
    output_arr = []
    if n == 1:
        return output_arr.append([1])
    else:
        for i in range(n):
            for j in range(i+1):
                arr = []
                arr.append(combination(i+1, j))
            output_arr.append(arr)
    return output_arr
