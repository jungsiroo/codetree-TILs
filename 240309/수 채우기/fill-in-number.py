import sys
input = sys.stdin.readline

def solution():
    answer = 0
    five, rest = divmod(n, 5)
    answer += five

    two, rest = divmod(rest,2)
    if rest != 0:
        return -1
        
    answer += two
    return answer


if __name__ == "__main__":
    n = int(input())

    print(solution())