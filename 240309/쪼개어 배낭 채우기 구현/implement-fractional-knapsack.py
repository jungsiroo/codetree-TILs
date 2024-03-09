import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def knapsack(jewels, m):
    heapq = []

    for jewel in jewels:
        w, v = jewel
        heappush(heapq, [-(v/w), w, v])

    answer = 0
    while m>0 and heapq:
        value_per_w, w, v = heappop(heapq)
        value_per_w *= -1

        if m>=w:
            m -= w
            answer += v
        else:
            value = v*(m/w)
            answer += value
            m = 0

    return format(round(answer, 3), ".3f")

if __name__ == "__main__":
    n, m = map(int, input().split())

    jewels = []
    for _ in range(n):
        jewels.append(list(map(int, input().split())))
    
    print(knapsack(jewels, m))