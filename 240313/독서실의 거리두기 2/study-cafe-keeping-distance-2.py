import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    seats = list(map(int, list(input().strip())))

    used = []

    for i in range(n):
        if seats[i] == 1:
            used.append(i)
    
    if len(used) == 1:
        if (n-1)-used[0] >= used[0]:
            seats[n-1] = 1
        else:
            seats[0] = 1
    else:
        prev = used[0]
        gap, start, end = [0]*3

        for now in used:
            if now - prev > gap:
                gap = now-prev
                start = prev
                end = now
            prev = now
        
        mid = (start+end) // 2
        seats[mid] = 1

    answer = int(1e9)
    prev = 0
    start = 0

    if seats[0] == 1:
        start = 1

    for i in range(start, n):
        if seats[i] == 1:
            answer = min(i-prev, answer)
            prev = i
    
    print(answer)