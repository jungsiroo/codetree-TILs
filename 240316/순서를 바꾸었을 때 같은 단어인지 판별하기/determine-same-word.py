import sys
input = sys.stdin.readline

def solution(a, b):
    if len(a) != len(b):
        return "No"

    dict_a, dict_b = dict(), dict()

    for s1, s2 in zip(a, b):
        dict_a[s1] = dict_a.get(s1, 0) + 1
        dict_b[s2] = dict_b.get(s2, 0) + 1
    
    if dict_a != dict_b:
        return "No"
    
    return "Yes"


if __name__ == "__main__":
    a = input().strip()
    b = input().strip()

    print(solution(a, b))