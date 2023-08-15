def battleship(grid: list[list[int]], line: int, column: int) -> bool:
    # raise NotImplementedError
    if grid[line][column] == 0:
        return False
    else:
        return True


# grid = [[0, 0, 0, 0, 1],
#         [0, 0, 0, 0, 1],
#         [1, 1, 1, 1, 1],
#         [0, 0, 0, 1, 0]]
# print(battleship(grid, 0, 0))
