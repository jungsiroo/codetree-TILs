import sys
input = sys.stdin.readline


BOMB = [
        [[-2,0], [-1, 0], [1,0], [2,0]],
        [[-1,0], [1,0], [0,-1], [0,1]],
        [[-1,-1], [-1,1], [1,-1], [1,1]]
    ]

def set_combination(now, cnt):
    global comb
    if cnt == len(bombs):
        comb.append(now)
        return

    for i in range(3):
        set_combination(now+[i], cnt+1)

def explode(b_type, r, c):
    global tmp

    for dx, dy in BOMB[b_type]:
        nr, nc = r+dx, c+dy
        if nr<0 or nr>=n or nc<0 or nc>=n:
            continue
        tmp[nr][nc] = 1 


if __name__ == "__main__":
    global comb, tmp

    n = int(input())
    board, comb = [], []
    tmp = []


    bombs = []
    for i in range(n):
        line = list(map(int, input().split()))

        for j in range(n):
            if line[j] == 1:
                bombs.append([i,j])
        board.append(line)
    
    set_combination([], 0)

    answer = 0
    for com in comb:
        tmp = [b[:] for b in board]

        for bomb, (r, c) in zip(com, bombs):
            explode(bomb, r, c)

        cnt = 0 
        for i in range(n):
            for j in range(n):
                if tmp[i][j] == 1:
                    cnt += 1
        answer = max(answer, cnt)
        
    print(answer)