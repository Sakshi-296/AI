
def dfs(m, c, boat, visited):
    state = (m, c, boat)

    if state in visited:
        return False

    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if (m > 0 and m < c) or (3-m > 0 and 3-m < 3-c):
        return False

    visited.add(state)
    print(state)

    if m == 0 and c == 0 and boat == 0:
        print("Goal Reached!")
        return True

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for x, y in moves:
        if boat == 1:
            if x <= m and y <= c:
                if dfs(m-x, c-y, 0, visited):
                    return True
        else:
            if x <= 3-m and y <= 3-c:
                if dfs(m+x, c+y, 1, visited):
                    return True

    return False

dfs(3, 3, 1, set())
