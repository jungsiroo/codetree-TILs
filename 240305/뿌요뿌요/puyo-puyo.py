import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def in_range(r, c):
    if r<0 or r>=n or c<0 or c>=n:
        return False
    return True

def dfs(r, c, val):
    global visited, answer, check, count 
    count += 1
    answer = max(answer, count)

    if count >= 4:
        check = True

    for i in range(4):
        nr, nc = r+dx[i], c+dy[i]

        if not in_range(nr, nc):
            continue
        if visited[nr][nc] or board[nr][nc] != val:
            continue
        visited[nr][nc] = True
        dfs(nr, nc, val)



if __name__ == "__main__":
    n = int(input())
    board = []

    global visited, answer, check, count
    visited = [[False]*n for _ in range(n)]
    answer = 0
    pop = 0

    for _ in range(n):
        board.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                check = False
                count = 0
                dfs(i, j, board[i][j])

                if check:
                    pop += 1

    print(pop, answer)