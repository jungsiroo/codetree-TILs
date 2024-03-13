import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    seats = list(map(int, list(input().strip())))

    gap, prev, start, end = [0]*4

    for i in range(n):
        if seats[i] == 1:
            if i-prev > gap:
                gap = i-prev
                start = prev
                end = i
            prev = i

    mid = (start+end) // 2
    seats[mid] = 1

    prev, gap = 0, int(1e9)
    answer = 0

    for i in range(1, n):
        if seats[i] == 1:
            if i-prev < gap:
                gap = i-prev
                answer = max(answer, gap)
            prev = i
    
    print(answer)