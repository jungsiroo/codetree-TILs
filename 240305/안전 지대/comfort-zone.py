import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def change(k):
    grid = [b[:] for b in board]

    for i in range(n):
        for j in range(m):
            if grid[i][j] <= k:
                grid[i][j] = 0
    
    return grid

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def in_range(r, c):
    if r<0 or r>=n or c<0 or c>=m:
        return False
    return True

def dfs(r, c, k):
    global visited

    for i in range(4):
        nr, nc = r+dx[i], c+dy[i]
        if not in_range(nr, nc):
            continue
        if visited[nr][nc] or board[nr][nc] <= k:
            continue
        visited[nr][nc] = True
        dfs(nr, nc, k)


if __name__ == "__main__":
    n, m = map(int, input().split())

    global visited
    board = []
    answer = []

    for _ in range(n):
        board.append(list(map(int, input().split())))

    MAX = max(sum(board, [])) 

    for k in range(1, MAX+1):
        visited = [[False]*m for _ in range(n)]
        area = 0

        for i in range(n):
            for j in range(m):
                if board[i][j] > k and not visited[i][j]:
                    visited[i][j] = True
                    dfs(i, j, k)
                    area += 1

        heappush(answer, [-area, k])             
    
    ans, k = heappop(answer)
    print(k, -ans)