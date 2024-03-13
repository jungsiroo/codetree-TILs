import sys
input = sys.stdin.readline

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    arr.sort()

    l_dist, r_dist = arr[1]-arr[0], arr[2]-arr[1]

    choice = -1
    answer = 0

    while l_dist != 1 or r_dist != 1:
        if l_dist == 1:
            choice = 0
        elif r_dist == 1:
            choice = 2
        else:
            if l_dist >= r_dist:
                choice = 0
            else:
                choice = 2

        direction = 2 if choice == 0 else -2  
        mid = arr[1] + direction
        if mid == arr[2-choice]:
            mid -= 1 if choice == 0 else -1
        arr[choice] = arr[1]
        arr[1] = mid

        l_dist, r_dist = arr[1]-arr[0], arr[2]-arr[1]
        answer += 1

    print(answer)