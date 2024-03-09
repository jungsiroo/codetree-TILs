import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    prices = list(map(int, input().split()))

    buy = prices[0]
    answer = 0

    for price in prices:
        if price-buy < 0:
            buy = price
        else:
            answer = max(answer, price-buy)
    
    print(answer)