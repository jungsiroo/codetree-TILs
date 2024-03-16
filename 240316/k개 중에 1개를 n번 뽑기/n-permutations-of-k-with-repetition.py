import sys
input = sys.stdin.readline

def solve(now, cnt):
    global answer
    if cnt == n:
        answer.append(now)
        return

    for i in range(1, k+1):
        solve(now+[i], cnt + 1)
        
if __name__ == "__main__":
    k, n = map(int, input().split())

    global answer
    answer = []

    solve([], 0)

    for ans in answer:
        print(*ans)