import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    answer = 0
    dp = [0]*n
    dp[0] = nums[0]

    for i in range(1, n):
        dp[i] = max(dp[i-1]+nums[i],nums[i])
    
    print(dp[i])