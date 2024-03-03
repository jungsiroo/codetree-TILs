import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def in_range(r, c):
    if r<0 or r>=n or c<0 or c>=m:
        return False
    return True

def dfs(row, col):
    global visited, answer

    if row == n-1 and col == m-1:
        return True

    for i in range(4):
        nr, nc = row+dx[i], col+dy[i]
        if not in_range(nr, nc):
            continue
        if board[nr][nc] == 0 or visited[nr][nc]:
            continue
        visited[nr][nc] = True
        answer |= dfs(nr, nc)

    return False



if __name__ == "__main__":
    global visited, answer
    answer = False

    n, m = map(int, input().split())

    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    

    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True

    dfs(0,0)
    print(int(answer))