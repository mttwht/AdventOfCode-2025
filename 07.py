from lib import file, grid

lines = file.readlines()

(sx, sy) = grid.find('S', lines)

beams = [(sx, sy)]
splitters = []

for (bx, by) in beams:
    for y in range(by+1, len(lines)):
        if lines[y][bx] == '^':
            if (bx, y) not in splitters:
                splitters.append((bx, y))
                beams.append((bx-1, y))
                beams.append((bx+1, y))
            break

print(len(splitters))
