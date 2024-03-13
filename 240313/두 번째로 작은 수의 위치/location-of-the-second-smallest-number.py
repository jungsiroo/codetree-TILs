import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(key):
    if key == -1 or key not in order or len(order[key])>1:
        return -1
    return order[key][0]

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    order = defaultdict(list)

    for i in range(n):
        order[nums[i]].append(i+1)

    nums.sort()
    smallest = nums[0]

    key = -1
    for i in range(n):
        if nums[i] > smallest:
            key = nums[i]
            break
    

    print(solution(key))