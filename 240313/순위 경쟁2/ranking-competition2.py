import sys
input = sys.stdin.readline

A = -1
TWIN = 0
B = 1

def get_status(value):
    if value>0:
        return 1
    elif value < 0:
        return -1
    return 0

if __name__ == "__main__":
    n = int(input())

    scores = [0, 0]

    answer = 0
    status = TWIN
    idx = 0
    
    for _ in range(n):
        c, s = input().split()
        s = int(s)

        if c == 'A':
            idx = 0
        else:
            idx = 1
        
        scores[idx] += s

        if get_status(scores[1] - scores[0]) != status:
            answer += 1
            status = get_status(scores[1]-scores[0]) 

    print(answer)