import sys
input = sys.stdin.readline

if __name__ == "__main__":
    line = list(map(int, input().split()))
    line.sort()

    choice = -1
    r_dist, l_dist = line[1] - line[0], line[2]-line[1]

    if r_dist <= l_dist:
        choice = 0
    else:
        choice = 2

    answer = 0 

    while r_dist != 1 or l_dist != 1:
        move = 1 if choice == 0 else -1
        nxt = line[1] + move

        line[choice] = line[1]
        line[1] = nxt

        r_dist, l_dist = line[1] - line[0], line[2]-line[1]

        answer += 1
    print(answer)