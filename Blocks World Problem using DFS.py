
def dfs(state, goal, visited):
    if state in visited:
        return False

    visited.add(state)
    print(state)

    if state == goal:
        print("Goal reached!")
        return True

    for i in range(len(state) - 1):
        new_state = list(state)
        new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
        new_state = tuple(new_state)

        if dfs(new_state, goal, visited):
            return True

    return False


start = ('A', 'B', 'C')
goal = ('C', 'B', 'A')

dfs(start, goal, set())
