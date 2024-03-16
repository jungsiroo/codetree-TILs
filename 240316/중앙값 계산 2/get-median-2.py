import sys
from heapq import heappop, heappush
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    min_heap, max_heap = [], []

    for i in range(n):
        if len(min_heap) == len(max_heap):
            heappush(max_heap, -nums[i])
        else:
            heappush(min_heap, nums[i])

        if min_heap and min_heap[0] < -max_heap[0]:
            min_val = heappop(min_heap)
            max_val = heappop(max_heap)

            heappush(min_heap, -max_val)
            heappush(max_heap, -min_val)
        
        if i%2 == 0:
            print(-max_heap[0], end=' ')