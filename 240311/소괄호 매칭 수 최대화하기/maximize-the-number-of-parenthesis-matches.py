import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def calculate_score(bracket):
    dp = [0] * len(bracket)
    dp[0] = int(bracket[0] == ")")

    for i in range(1, len(bracket)):
        dp[i] = dp[i-1]
        if bracket[i] == ")":
            dp[i] += 1
    
    answer = 0

    for i in range(len(bracket)):
        if bracket[i] == "(":
            answer += (dp[-1] - dp[i])
    
    return answer
    
if __name__ == "__main__":
    n = int(input())
    strings = []

    for _ in range(n):
        string = input().strip()
        heappush(strings, [-string.count('(')/len(string), string])

    bracket = '' 
    while strings:
        _, string = heappop(strings)
        bracket += string

    print(calculate_score(bracket))