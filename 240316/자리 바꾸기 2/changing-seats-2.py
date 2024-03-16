import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k =map(int, input().split())

    history = [set([i]) for i in range(n+1)]
    seats = [i for i in range(n+1)]

    change = []
    for _ in range(k):
        a, b = map(int, input().split())
        change.append([a, b])
    
    for _ in range(3):
        for a, b in change:
            seats[b], seats[a] = seats[a], seats[b]

            history[seats[a]].add(a)
            history[seats[b]].add(b)

    for i in range(1, n+1):
        print(len(history[i]))