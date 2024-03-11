import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    meetings = []

    for _ in range(n):
        meetings.append(list(map(int, input().split())))
    meetings.sort()

    dp = [[0, 0, 1] for _ in range(n)] # start, end, value
    dp[0] = [*meetings[0], 1]

    for i, (start, end) in enumerate(meetings[1:],1):
        if start>=dp[i-1][1]:
            dp[i] = [start, end, dp[i-1][2]+1]
        else:
            index = -1
            for j in range(i, -1, -1):
                if dp[j][1]<=start:
                    index =  j
                    break
            
            dp[i] = [start, end, dp[index][2]+1]
            if index == -1:
                dp[i] = [start, end, 1]

    print(n-dp[n-1][2])