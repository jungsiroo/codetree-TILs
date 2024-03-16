import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, g = map(int, input().split())
    visited = set([1])

    answer = 0
    for _ in range(g):
        inp = list(map(int, input().split()))
        total, people = inp[0], set(inp[1:])

        if total - len(visited.intersection(people)) == 1:
            visited = visited.union(people)
            # print(visited)

    print(len(visited))