import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = [str(input().strip()) for _ in range(n)]
    nums.sort(key=lambda x:x*9, reverse=True)

    print(''.join(nums))