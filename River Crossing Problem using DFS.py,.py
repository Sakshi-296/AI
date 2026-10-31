
def safe(s):
    f, w, g, c = s
    return not ((w == g and f != w) or (g == c and f != g))

def dfs(s, visited):
    if s == (1, 1, 1, 1):
        print(s)
        print("Goal Reached!")
        return True

    if s in visited:
        return False

    visited.add(s)
    print(s)

    for move in [(1,0,1,0), (1,1,0,0), (1,0,0,1), (1,0,0,0)]:
        n = tuple(s[i] ^ move[i] for i in range(4))

        if safe(n) and dfs(n, visited):
            return True

    return False

dfs((0,0,0,0), set())
