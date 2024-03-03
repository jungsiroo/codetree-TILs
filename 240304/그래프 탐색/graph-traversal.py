import sys
input = sys.stdin.readline

def dfs(now):
    global visited

    if visited[now]:
        return 1
    visited[now] = True

    answer = 0
    for node in adj[now]:
        visited[node] = True

        answer += dfs(node)
    
    return answer


if __name__ == "__main__":
    n, m = map(int, input().split())

    global visited

    adj = [[] for _ in range(n+1)]
    visited = [False]*(n+1)

    for _ in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    print(dfs(1))