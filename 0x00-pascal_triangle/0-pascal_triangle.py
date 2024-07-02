#!/usr/bin/python3


def pascal_triangle(n):
    """
    Generates Pascal's triangle of n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    # If n is less than or equal to 0, return an empty list.
    if n <= 0:
        return []

    # Initialize an empty list to store the triangle.
    triangle = []

    # Iterate over each row of the triangle.
    for i in range(n):
        # Initialize an empty list to store the current row.
        row = []

        # Iterate over each element in the current row.
        for j in range(i + 1):
            # If the current element is the first or last element in the row,
            # set its value to 1.
            if j == 0 or j == i:
                row.append(1)
            # Otherwise, calculate the value of the element by summing the
            # corresponding elements in the previous row of the triangle.
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # Add the current row to the triangle.
        triangle.append(row)

    # Return the complete Pascal's triangle.
    return triangle
