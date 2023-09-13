#!/usr/bin/python3
"""pascal triangle function:"""


def pascal_triangle(n):
    """returns list of lists of ints representing pascal"""
    if n <= 0:
        return []

    triangle = []
    line = []
    for i in range(n):
        line = [1]
        if i > 0:
            for j in range(i):
                ele = sum(triangle[-1][j:j+2])
                line.append(ele)
        triangle.append(line)
    return triangle
