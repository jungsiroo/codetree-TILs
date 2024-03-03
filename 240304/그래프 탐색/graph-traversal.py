import sys
input = sys.stdin.readline

def dfs(now, count):
    global visited

    if visited[now]:
        return count

    answer = 0
    for node in adj[now]:
        visited[node] = True
        answer += dfs(node, count+1)

    return answer


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

    print(dfs(1, 0))