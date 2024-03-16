import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    dp = dict()

    for num in nums:
        dp[num] = dp.get(num, 0)+1

    answer = 0 
    for i in range(n-2):
        dp[nums[i]] = max(dp.get(nums[i])-1, 0)
        for j in range(i+1, n-1):
            dp[nums[j]] = max(dp.get(nums[j])-1,0)
            target = k - (nums[i] + nums[j])
            answer += dp.get(target,0)
    
    print(answer)