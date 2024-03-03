import sys
input = sys.stdin.readline

def dfs(now):
    global visited, answer

    for node in adj[now]:
        if visited[node]:
            continue

        visited[node] = True
        answer += 1
        dfs(node)


if __name__ == "__main__":
    n, m = map(int, input().split())

    global visited, answer
    answer =0 

    adj = [[] for _ in range(n+1)]
    visited = [False]*(n+1)

    for _ in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    visited[1] = True
    dfs(1)
    print(answer)