import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    seats = list(map(int, list(input().strip())))

    used = []

    for i in range(n):
        if seats[i] == 1:
            used.append(i)
    
    if len(used) == 1:
        if (n-1)-used[0] >= used[0]:
            seats[n-1] = 1
            used.append(n-1)
        else:
            seats[0] = 1
            used.append(0)
    else:
        prev = used[0]
        gap, start, end = [0]*3

        for now in used:
            if now - prev > gap:
                gap = now-prev
                start = prev
                end = now
            prev = now

        left = used[0]    
        right = n-1-used[-1]
        mid = end-(start+end)//2

        max_choice = max(left, mid, right)
        if max_choice == left:
            seats[0] = 1
            used.append(0)
        elif max_choice == mid:
            seats[(start+end)//2] = 1
            used.append((start+end)//2)
        else:
            seats[-1] = 1
            used.append(n-1)
        
    used.sort()

    prev, answer = used[0], int(1e9)

    for now in used[1:]:
        answer = min(answer, now-prev)
        prev = now
    
    print(answer)