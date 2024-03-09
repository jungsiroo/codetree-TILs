import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    m = 0
    nums = dict()

    for _ in range(n):
        x, y = map(int, input().split())
        m += x
        nums[y] = nums.get(y, 0)+x

    nums = dict(sorted(nums.items(), key=lambda x:x[0]))
    keys = list(nums.keys())

    start, end = 0, len(keys)-1

    answer = 0

    for _ in range(m//2):
        k1, k2 = keys[start], keys[end]
        answer = max(answer, (k1+k2))

        nums[k1] -= 1
        nums[k2] -= 1

        if nums[k1] == 0:
            start += 1
        if nums[k2] == 0:
            end -= 1
        
    print(answer)