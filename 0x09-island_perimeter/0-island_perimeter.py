#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid where 1 represents land and 0 represents water.

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
                # If it's the first row or the cell above is water (0), add to perimeter
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                # Check the cell below (down)
                # If it's the last row or the cell below is water (0), add to perimeter
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

                # Check the cell to the left
                # If it's the first column or the cell to the left is water (0), add to perimeter
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                # Check the cell to the right
                # If it's the last column or the cell to the right is water (0), add to perimeter
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    # Return the total calculated perimeter
    return perimeter
