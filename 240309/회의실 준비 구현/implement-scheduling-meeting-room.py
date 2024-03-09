import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    meetings = []

    for _ in range(n):
        start, end = map(int, input().split())
        meetings.append([start, end])

    meetings.sort(key=lambda x:x[1])

    answer = 0 
    prev = 0

    for meeting in meetings:
        start, end = meeting
        if start>= prev:
            answer += 1
            prev = end
    
    print(answer)