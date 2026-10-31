
from heapq import *

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(state):
    return sum(state[i] != goal[i] and state[i] != 0 for i in range(9))

queue = [(h(start), 0, start)]
visited = set()

while queue:
    f, g, state = heappop(queue)

    if state == goal:
        print("Goal Reached!")
        print(state)
        break

    if state in visited:
        continue

    visited.add(state)
    print(state)

    zero = state.index(0)

    for move in [-3, 3, -1, 1]:
        new = zero + move

        if 0 <= new < 9 and abs(zero // 3 - new // 3) + abs(zero % 3 - new % 3) == 1:
            s = list(state)
            s[zero], s[new] = s[new], s[zero]
            s = tuple(s)

            if s not in visited:
                heappush(queue, (g + 1 + h(s), g + 1, s))
