import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    hash_map = set()

    for num in nums:
        hash_map.add(num)

    answer = 0
    for num in nums:
        target = k - num

        if target in hash_map:
            answer += 1
            hash_map.remove(num)
            hash_map.remove(target)

    print(answer)