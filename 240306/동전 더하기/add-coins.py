import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())

    coins = []
    for _ in range(n):
        coins.append(int(input()))

    coins.sort(reverse=True)

    index = 0
    answer = 0

    while k>0:
        mok, div = divmod(k, coins[index])
        k -= mok*coins[index]
        answer += mok
        index += 1

    print(answer)