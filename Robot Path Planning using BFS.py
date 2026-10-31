
from collections import deque

grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]

start = (0, 0)
goal = (2, 2)

queue = deque([(start, [start])])
visited = {start}

while queue:
    (x, y), path = queue.popleft()

    if (x, y) == goal:
        print("Path:", path)
        print("Steps:", len(path) - 1)
        break

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy

        if (0 <= nx < 3 and 0 <= ny < 3
                and grid[nx][ny] == 0
                and (nx, ny) not in visited):

            visited.add((nx, ny))
            queue.append(((nx, ny), path + [(nx, ny)]))
else:
    print("No path found")
