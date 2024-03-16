import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    a_cnt, b_cnt = dict(), dict()

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for num in a:
        a_cnt[num] = a_cnt.get(num,0)+1

    for num in b:
        b_cnt[num] = b_cnt.get(num,0)+1

    if a_cnt == b_cnt:
        print("Yes")
    else:
        print("No")