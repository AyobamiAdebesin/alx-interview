#!/usr/bin/python3
import time

def factorial(n):
    """
    Compute the factorial of n
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0 or n == 0:
        return 1
    else:
        fact = n * factorial(n-1)
        return fact


def combination(n, r):
    """
    Compute the combinatorial coefficients
    """
    if not isinstance(n, int) or not isinstance(r, int):
        raise TypeError("n and r must be integers")
    return int(factorial(n)/(factorial(n-r)*factorial(r)))


def pascal_triangle(n):
    """
    Construct the pascal triangle of height n
    """
    start = time.time()
    output_arr = []
    if not isinstance(n, int):
        return output_arr
    if n <= 0:
        return output_arr

    for i in range(n):
        arr = []
        for j in range(i+1):
            arr.append(combination(i, j))
        output_arr.append(arr)
    end = time.time()

    print("Time taken to run: ", end-start)
    return output_arr
