import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k, T = input().split()
    n = int(n)
    k = int(k)

    answer = []
    for _ in range(n):
        string = input().strip()

        if string.startswith(T):
            answer.append(string)
    
    print(sorted(answer)[k-1])