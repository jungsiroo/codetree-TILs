import sys
from string import ascii_uppercase as UPPER
input = sys.stdin.readline

if __name__ == "__main__":
    order = {S:i for i, S in enumerate(UPPER)}

    n = int(input())
    arr = input().split()

    answer = 0

    for i in range(n):
        for j in range(i+1, n):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                answer += 1

    print(answer)