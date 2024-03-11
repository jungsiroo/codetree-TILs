import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    a, b, x, y = map(int, input().split())

    dist = [int(1e9)]*101
    dist[a] = 0
    queue = deque()
    queue.append([a, True])


    while queue:
        now, used = queue.popleft()

        if now == x and not used:
            if dist[y] < dist[now]+1:
                continue
            dist[y] = dist[now]+1
            queue.append([y, True])
        
        elif now == y and not used:
            if dist[x] < dist[now]+1:
                continue
            dist[x] = dist[now]+1
            queue.append([x, True])

        else:
            for nxt in [-1, 1]:
                if now+nxt<0 or now+nxt>100:
                    continue
                
                if dist[now+nxt] < dist[now+1]:
                    continue

                dist[now+nxt] = dist[now+1]
                queue.append([now+nxt, used])

    print(dist[b])