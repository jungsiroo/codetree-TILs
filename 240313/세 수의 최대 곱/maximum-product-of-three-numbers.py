import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    zero_check = int(nums.count(0) > 0)

    answer = 0 if zero_check else -int(1e9)
    answer = max(answer, nums[0]*nums[1]*nums[-1])
    answer = max(answer, nums[-1]*nums[-2]*nums[-3])

    print(answer)