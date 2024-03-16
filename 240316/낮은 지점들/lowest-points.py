import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    coor = dict()

    for _ in range(n):
        x, y = map(int, input().split())
        coor[x] = min(coor.get(x, int(1e9)), y)

    print(sum(coor.values()))