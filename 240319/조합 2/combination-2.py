import sys
input = sys.stdin.readline

MOD = 10007

def dfs(left, right):
    global dp

    if left == right or left == 1 or right == 0:
        dp[tuple([left, right])] = 1
        return 1
    
    if right == 1:
        dp[tuple([left, right])] = left
        return left
    
    if tuple([left, right]) in dp:
        return dp[tuple([left, right])]
    
    dp[tuple([left, right])] = dfs(left-1, right) + dfs(left-1, right-1)
    return dp[tuple([left, right])]

if __name__ == "__main__":
    n, m = map(int, input().split())

    global dp
    dp = dict()

    dfs(n, m)

    print(dp[tuple([n,m])] % MOD)