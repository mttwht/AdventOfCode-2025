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

def find(target: str, grid: list[str]) -> tuple[int, int] | None:
    """
    Find the position of a target character in a 2D grid.

    Parameters:
    target (str): The character to search for.
    grid (list of str): The 2D grid represented as a list of strings.

    Returns:
    tuple of int: A tuple (x, y) representing the position of the target character,
                  or None if the character is not found.
    """
    for y, row in enumerate(grid):
        if target in row:
            return (row.index(target), y)
    return None
