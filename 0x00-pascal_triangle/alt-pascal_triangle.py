import math


# Using Dynamic Programming
# Uses a 2D list to store the triangle, and
# iterates over each row and column to calculate the values using dynamic programming.
def pascal_triangle_1(n):
    triangle = [[1 for _ in range(i + 1)] for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle


# Using Mathematical Computations
def pascal_triangle_2(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(math.comb(i, j))
        triangle.append(row)
    return triangle
