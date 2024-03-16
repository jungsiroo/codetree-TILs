import sys
input = sys.stdin.readline

def make_comb(now, idx, cnt):
    global comb
    if cnt == 3:
        comb.append(now)
        return

    for i in range(idx+1, m):
        if visited[i]:
            continue
        visited[i] = True
        make_comb(now + [i], i, cnt + 1)
        visited[i] = False



if __name__ == "__main__":
    global comb, visited

    n, m = map(int, input().split())
    arr1, arr2 = [], []

    comb = []
    visited = [False]*m

    for _ in range(n):
        arr1.append(list(input().strip()))

    for _ in range(n):
        arr2.append(list(input().strip()))

    make_comb([], -1, 0)

    answer = 0

    for i, j, k in comb:
        group1 = set()
        check = True

        for idx in range(n):
            group1.add(arr1[idx][i]+arr1[idx][j]+arr1[idx][k])

        for idx in range(n):
            if (arr2[idx][i]+arr2[idx][j]+arr2[idx][k]) in group1:
                check = False
                break

        if check:
            answer += 1

    print(answer)