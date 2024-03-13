import sys
from string import ascii_uppercase as UPPER
input = sys.stdin.readline

if __name__ == "__main__":
    order = {S:i for i, S in enumerate(UPPER)}

    n = int(input())
    arr = input().split()

    answer = 0

    # for i in range(n):
    #     s = arr[i]
    #     if order[s] != i:
    #         arr[i], arr[order[s]] = arr[order[s]], arr[i]
    #         answer += 1

    check = [0]*n
    index = set()
    for i in range(n):
        if order[arr[i]] == i:
            check[i] =1 
        else:
            index.add(i)
    
    sum_check = sum(check)
    alphabet = list(UPPER)
    
    while sum_check != n:
        idx = next(iter(index))
        s = arr[idx]
        arr[idx], arr[order[s]] = arr[order[s]], arr[idx]


        if arr[idx] == alphabet[idx]:
            sum_check += 1
            index.remove(idx)
        if arr[order[s]] == alphabet[order[s]]:
            sum_check += 1
            index.remove(order[s])

        answer += 1 

    
    print(answer)