import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    queue = []
    for _ in range(n):
        start, end = map(int, input().split())
        queue.append([start, 1])
        queue.append([end, -1])

    queue.sort()

    cnt = 0
    ans = 0

    for x, v in queue:
        cnt += v

        if v == 1:
            ans = max(ans, cnt)
    
    print(ans)