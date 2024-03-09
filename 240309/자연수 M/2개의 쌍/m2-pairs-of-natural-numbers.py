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

    while start <= end:
        k1, k2 = keys[start], keys[end]
        answer = max(answer, (k1+k2))

        if nums[k1] == nums[k2]:
            start += 1
            end -= 1
        
        elif nums[k1] < nums[k2]:
            start += 1
            nums[k2] -= nums[k1]
        
        else:
            end -= 1
            nums[k1] -= nums[k2]
        
    print(answer)