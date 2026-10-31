
def dfs(a, b, visited):
    if (a, b) in visited:
        return False

    visited.add((a, b))
    print("Jug A:", a, "Jug B:", b)

    if a == 2 or b == 2:
        print("Goal Reached!")
        return True

    return (
        dfs(4, b, visited) or
        dfs(a, 3, visited) or
        dfs(0, b, visited) or
        dfs(a, 0, visited) or
        dfs(max(0, a - (3 - b)), min(3, a + b), visited) or
        dfs(min(4, a + b), max(0, b - (4 - a)), visited)
    )

visited = set()
dfs(0, 0, visited)
