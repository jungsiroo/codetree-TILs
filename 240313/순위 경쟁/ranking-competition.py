import sys
input = sys.stdin.readline

def get_idx(c):
    return ord(c)-65

def transform(scores):
    ret = [0]*3
    max_val = max(scores)
    
    for i in range(3):
        if scores[i] == max_val:
            ret[i] = 1

    return ret

if __name__ == "__main__":
    n = int(input())
    scores = [0, 0, 0]
    status = [1]*3
    answer= 0

    for _ in range(n):
        c, s = input().split()
        s = int(s)

        scores[get_idx(c)] += s
        trans = transform(scores)
        
        if trans != status:
            answer += 1
        status = trans[:]
    
    print(answer)