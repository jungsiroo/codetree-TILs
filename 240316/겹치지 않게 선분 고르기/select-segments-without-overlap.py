import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    lines = []

    for _ in range(n):
        lines.append(list(map(int, input().split())))

    lines.sort(key=lambda x:(x[1], x[0]))

    prev = -1
    answer = 0

    for start, end in lines:
        if start > prev:
            answer += 1
            prev = start

    print(answer)