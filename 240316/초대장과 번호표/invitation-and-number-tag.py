import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n, g = map(int, input().split())
    visited = set([1])

    answer = 0
    save = deque()

    for _ in range(g):
        inp = list(map(int, input().split()))
        total, people = inp[0], set(inp[1:])
        save.append([total, people, 0, 0])

    while save:
        total, people, now, prev = save.popleft()

        if (now == prev) and (now+prev > 0):
            continue
        
        inter = len(visited.intersection(people))
        if total - inter == 1:
            visited.update(people)
        else:
            save.append([total, people, inter, now])
        # print(visited)

    print(len(visited))