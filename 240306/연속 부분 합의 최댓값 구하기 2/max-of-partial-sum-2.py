import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = [0]+list(map(int, input().split()))

    answer = -987654321
    sum_num = 0

    for i in range(1, n+1):
        if sum_num < 0:
            sum_num = nums[i]
        else:
            sum_num += nums[i]
        
        answer = max(answer, sum_num)

    print(answer)