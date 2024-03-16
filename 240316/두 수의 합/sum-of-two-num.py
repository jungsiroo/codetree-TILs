import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    hash_map = dict()

    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1

    answer = 0

    for num in nums:
        target = k- num
        answer += hash_map.get(target, 0)
        hash_map[num] = max(hash_map.get(num,0) -1, 0)


    print(answer)