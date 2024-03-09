import sys
from heapq import heappush, heappop
input = sys.stdin.readline

if __name__ == "__main__":
    c, n = map(int, input().split())

    red, black = [], []

    for _ in range(c):
        red.append(int(input()))

    red.sort()

    for _ in range(n):
        a, b = map(int, input().split())
        black.append([a, b])
    
    black.sort(key=lambda x:(x[0], abs(x[0]-x[1])))

    answer = 0
    r_idx, b_idx= 0, 0

    while r_idx<c and b_idx<n:
        t = red[r_idx]
        a, b = black[b_idx]

        if a<=t<=b:
            answer += 1
            r_idx += 1
            b_idx += 1
        else:
            if t<a:
                r_idx += 1
            elif t>b:
                b_idx += 1


    print(answer)