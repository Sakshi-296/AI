
grid = [
    ['S', '.', '.', '.'],
    ['.', '#', '.', '.'],
    ['.', '.', '.', '.'],
    ['.', '#', '#', 'G']
]

position = (0, 0)
visited = set()

print("Starting position:", position)

while position != (3, 3):
    r, c = position
    visited.add(position)

    moves = [
        (r, c + 1),
        (r + 1, c),
        (r, c - 1),
        (r - 1, c)
    ]

    moved = False

    for nr, nc in moves:
        if (0 <= nr < 4 and 0 <= nc < 4
                and grid[nr][nc] != '#'
                and (nr, nc) not in visited):

            position = (nr, nc)
            print("Move to:", position)
            moved = True
            break

    if not moved:
        print("No path found!")
        break

if position == (3, 3):
    print("Goal reached!")
