import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    answer = 0

    start, end = 0, 2*n-1
    for _ in range(n):
        answer = max(answer, nums[start]+nums[end])
        start += 1
        end -= 1

    print(answer)