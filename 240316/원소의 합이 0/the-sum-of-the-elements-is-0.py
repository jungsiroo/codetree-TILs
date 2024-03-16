import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    nums = [[] for _ in range(4)]

    for i in range(4):
        nums[i] = list(map(int, input().split()))

    ab_pair = dict()

    for i in range(n):
        a_value = nums[0][i]
        for j in range(n):
            b_value = nums[1][j]
            ab_pair[(a_value + b_value)] = ab_pair.get(a_value+b_value, 0)+1

    cd_pair = dict()    

    for i in range(n):
        c_value = nums[2][i]
        for j in range(n):
            d_value = nums[3][j]
            cd_pair[(c_value + d_value)] = cd_pair.get(c_value+d_value, 0)+1

    answer = 0

    for ab_val, ab_cnt in ab_pair.items():
        for cd_val, cd_cnt in cd_pair.items():
            if ab_val + cd_val == 0:
                answer += ab_cnt*cd_cnt
                cd_pair[cd_val] -= cd_cnt
    print(answer)