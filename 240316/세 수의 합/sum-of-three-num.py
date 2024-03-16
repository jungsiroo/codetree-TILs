import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    dp = dict()

    for num in nums:
        dp[num] = dp.get(num, 0)+1

    answer = 0 
    for i in range(n):
        dp[nums[i]] = dp.get(nums[i],0)-1

        for j in range(i):
            target = k - (nums[i] + nums[j])
            answer += dp.get(target,0)

   
    print(answer)