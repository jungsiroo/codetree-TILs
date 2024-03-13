import sys
input = sys.stdin.readline

def solution():
    if L[0] == B[0]:
        return abs(B[1]-L[1])-1+int(R[0] == L[0])*2

    if L[1] == B[1]:
        return abs(B[0]-L[0])-1+int(R[1] == L[1])*2

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