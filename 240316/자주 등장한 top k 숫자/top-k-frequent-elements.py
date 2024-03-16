import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    dp = dict()
    for num in nums:
        dp[num] = dp.get(num,0) +1
    
    dp = dict(sorted(dp.items(), key=lambda x:(-x[1], -x[0])))

    for i, key in enumerate(dp.keys()):
        if i == k:
            break
        print(key, end=' ')