
from collections import deque

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

q = deque([(start, [])])
visited = {start}

while q:
    s, path = q.popleft()

    if s == goal:
        for state in path + [s]:
            for i in range(0, 9, 3):
                print(state[i:i+3])
            print()
        print("Total moves:", len(path))
        break

    z = s.index(0)

    for n in [z-3, z+3, z-1, z+1]:
        if 0 <= n < 9 and abs(z//3 - n//3) + abs(z%3 - n%3) == 1:
            a = list(s)
            a[z], a[n] = a[n], a[z]
            a = tuple(a)

            if a not in visited:
                visited.add(a)
                q.append((a, path + [s]))
