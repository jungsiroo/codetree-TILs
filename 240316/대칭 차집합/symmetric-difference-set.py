import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    answer = (a-b).union(b-a)
    print(len(answer))