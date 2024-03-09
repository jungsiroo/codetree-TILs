import sys
input = sys.stdin.readline

# 7 4 1 8 5 2 9 6 3

## 3301 -> 

def solution(n):
    answer = 0

    while n%5 != 0 and n>0:
        n -= 2
        answer += 1

    if n < 0:
        return -1
    five, rest = divmod(n, 5)
    answer += five

    two, rest = divmod(rest,2)
    if rest != 0:
        return -1
        
    answer += two
    return answer


if __name__ == "__main__":
    n = int(input())
    print(solution(n))