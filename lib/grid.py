def getNeighbours(
    x: int, y: int, grid: list[list[str]], diagonal: bool = False
) -> list[tuple[int, int]]:
    """
    Given a position (x, y) in a 2D grid, return the valid neighboring positions.
    Neighbors are considered to be the cells directly above, below, left, and right.

    Parameters:
    x (int): The x-coordinate (column index) of the position.
    y (int): The y-coordinate (row index) of the position.
    grid (list of list): The 2D grid represented as a list of lists.
    diagonal (bool): Whether to include diagonal neighbors.

    Returns:
    list of tuple: A list of tuples representing the valid neighboring positions.
    """
    neighbors = []
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Define possible movements: up, down, left, right
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if diagonal:
        # Add diagonal movements: up-left, up-right, down-left, down-right
        movements += [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dx, dy in movements:
        nx, ny = x + dx, y + dy
        if 0 <= nx < cols and 0 <= ny < rows:
            neighbors.append((nx, ny))

    return neighbors
