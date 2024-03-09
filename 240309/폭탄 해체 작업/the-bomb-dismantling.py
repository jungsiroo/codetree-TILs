import sys
input = sys.stdin.readline

if __name__ == "__main__": 
    n = int(input())
    bombs = []

    for _ in range(n):
        score, limit = map(int, input().split())
        bombs.append([score, limit])
    
    bombs.sort(key=lambda x:(x[1], -x[0]))

    now, answer = 0,  0
    for score, limit in bombs:
        if now<limit:
            answer += score
        now += 1

    print(answer)