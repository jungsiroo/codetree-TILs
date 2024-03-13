import sys
input = sys.stdin.readline

def solution():
    if L[0] == B[0]:
        min_w = min(L[1], B[1])
        max_w = max(L[1], B[1])
        return abs(B[1]-L[1])-1+int(R[0] == L[0] and min_w<R[1]<max_w)*2

    if L[1] == B[1]:
        min_h = min(L[0], B[0])
        max_h = max(L[0], B[0])
        return abs(B[0]-L[0])-1+int(R[1] == L[1] and min_h<R[0]<max_h)*2

    return abs(B[0]-L[0])+abs(B[1]-L[1])-1


if __name__ == "__main__":
    L, R, B = [[] for _ in range(3)]

    for i in range(10):
        line = input().strip()
        for j in range(10):
            if line[j] == 'L':
                L = [i, j]
            elif line[j] == 'R':
                R = [i, j]
            elif line[j] == 'B':
                B = [i, j]

    print(solution())