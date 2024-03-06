import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    answer = 0

    for i in range(n):
        answer += nums[i]

        if answer < 0 and i<n-1:
            answer = 0

    print(answer)