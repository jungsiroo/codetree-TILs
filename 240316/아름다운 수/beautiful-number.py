import sys
input= sys.stdin.readline

def check_continuous(now):
    prev = 0
    cnt = dict()

    for num in now:
        if num != prev:
            if prev != 0 and cnt[prev] % prev != 0:
                return False

            cnt[num] = 1
        else:
            cnt[num] += 1
        prev = num
    
    for k, v in cnt.items():
        if v%k != 0:
            return False

    return True

def beautiful(now, cnt):
    global answer
    if cnt == n:
        if check_continuous(now):
            answer += 1

        return

    for i in range(1, 5):
        beautiful(now+[i], cnt+1)


if __name__ == "__main__":
    n = int(input())

    global answer
    answer = 0
    beautiful([], 0)

    print(answer)