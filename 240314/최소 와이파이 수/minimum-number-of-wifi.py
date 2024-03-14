import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    i = 0
    answer = 0

    while i<n:
        if arr[i] == 1:
            answer += 1
            i += 2*m+1

        else:
            i+= 1
    print(answer)