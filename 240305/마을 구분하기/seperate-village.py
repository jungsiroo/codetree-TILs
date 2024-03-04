import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def in_range(r, c):
    if r<0 or r>=n or c<0 or c>=n:
        return False
    return True

def can_go(nr, nc):
    if not in_range(nr, nc):
        return False
    if visited[nr][nc] or board[nr][nc] == 0:
        return False
    
    return True

def dfs(r, c):
    global visited, answer, count

    for i in range(4):
        nr, nc = r+dx[i], c+dy[i]
        if not can_go(nr, nc):
            continue
            
        visited[nr][nc] = True
        count += 1
        dfs(nr, nc)
    
if __name__ == "__main__":
    n = int(input())
    global visited, answer, count

    answer = []
    visited = [[False]*n for _ in range(n)]

    board = []
    place = []

    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(n):
            if line[j] == 1:
                place.append([i, j])
        board.append(line)
    
    for r, c in place:
        if visited[r][c]:
            continue
        count = 1
        visited[r][c] = True
        dfs(r,c)
        answer.append(count)

    answer.sort()
    print(len(answer))
    for ans in answer:
        print(ans)