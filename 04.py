from lib import file, grid

map = file.readgrid()

accessible_rolls = []

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] != "@":
            continue
        
        paper_neighbours = 0
        for nx, ny in grid.getNeighbours(x, y, map, diagonal=True):
            if map[ny][nx] == "@":
                paper_neighbours += 1
                
        if paper_neighbours < 4:
            accessible_rolls.append((x, y))

print(len(accessible_rolls))
