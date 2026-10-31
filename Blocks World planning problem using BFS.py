
from collections import deque

start = ('A', 'B', 'C')
goal = ('C', 'B', 'A')

q = deque([start])
visited = {start}

while q:
    state = q.popleft()
    print(state)

    if state == goal:
        print("Goal reached!")
        break

    for i in range(2):
        s = list(state)
        s[i], s[i+1] = s[i+1], s[i]
        s = tuple(s)

        if s not in visited:
            visited.add(s)
            q.append(s)
