import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    blocks = []

    for _ in range(n):
        blocks.append(int(input()))
    
    mean = sum(blocks) // n
    answer = 0

    for i in range(n):
        if blocks[i] < mean:
            answer += mean-blocks[i]

    print(answer)