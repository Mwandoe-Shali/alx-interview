#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid 1 = land and 0 = water.

    Returns:
        int: The perimeter of the island.
    """
    # Initialize the perimeter counter
    perimeter = 0

    # Get the number of rows in the grid
    rows = len(grid)
    # Get the number of columns in the grid (if there are any rows)
    cols = len(grid[0]) if rows > 0 else 0

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is land (1)
            if grid[i][j] == 1:
                # Check the cell above (up)
                # If first row or cell above is water (0), add to perimeter
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                # Check the cell below (down)
                # If last row or cell below is water (0), add to perimeter
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

                # Check the cell to the left
                # If first col or cell to left = water (0), add to perimeter
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                # Check the cell to the right
                # If last col or cell to right = water (0), add to perimeter
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    # Return the total calculated perimeter
    return perimeter
