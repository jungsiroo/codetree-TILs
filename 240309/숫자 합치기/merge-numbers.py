import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int,input().split()))

    heapify(nums)

    answer = 0
    while nums:
        v1, v2 = heappop(nums), heappop(nums)
        answer += (v1+v2)

        if not nums:
            break
        heappush(nums, v1+v2)
        

    print(answer)