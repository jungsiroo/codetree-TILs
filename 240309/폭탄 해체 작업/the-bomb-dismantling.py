import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def get_score(idx):
    _, ret = bombs[idx]
    return ret

def get_limit_time(idx):
    ret, _ = bombs[idx]
    return ret

if __name__ == "__main__": 
    n = int(input())
    bombs = []

    for _ in range(n):
        score, limit = map(int, input().split())
        bombs.append([limit, score])
    
    bombs.sort()

    index = n-1
    MAX_T = 10000
    answer = 0
    pq = []

    for t in range(MAX_T, 0, -1):
        while index>=0 and get_limit_time(index)>=t:
            heappush(pq, -get_score(index))
            index -= 1

        if pq:
            answer -= heappop(pq)

    print(answer)