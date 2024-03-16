import sys
input= sys.stdin.readline

def get_continuous_cnt(now):
    prev = 0
    cnt = dict()

    for num in now:
        if num != prev:
            if prev != 0:
                cnt[prev] = cnt.get(prev,0)%prev
            cnt[num] = 1
        else:
            cnt[num] += 1
        prev = num

    return cnt

def beautiful(now, cnt):
    global answer
    if cnt == n:
        check = get_continuous_cnt(now)
        flag = True

        for key, value in check.items():
            if key == 0:
                continue
            if value%key != 0:
                flag = False
                break
        
        if flag:
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