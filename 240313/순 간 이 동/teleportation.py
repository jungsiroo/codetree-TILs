import sys
input = sys.stdin.readline

if __name__ == "__main__":
    a, b, x, y = map(int, input().split())

    answer = int(1e9)
    answer = min(answer, abs(b-a))
    answer = min(answer, abs(a-x)+abs(y-b))
    answer = min(answer, abs(a-y)+abs(x-b))
    
    print(answer)