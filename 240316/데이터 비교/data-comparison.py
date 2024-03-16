import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr1 = set(arr1)

    m = int(input())
    arr2 = list(map(int, input().split()))

    for num in arr2:
        print(int(num in arr1), end=' ')