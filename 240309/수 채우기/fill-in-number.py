import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    answer = 0
    five, rest = divmod(n, 5)
    answer += five

    answer += (rest//2)
    print(answer)