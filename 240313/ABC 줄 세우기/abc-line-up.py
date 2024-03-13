import sys
from string import ascii_uppercase as UPPER
input = sys.stdin.readline

if __name__ == "__main__":
    order = {S:i for i, S in enumerate(UPPER)}

    n = int(input())
    arr = input().split()


    alphabet = list(UPPER)
    answer = 0
    index = set()
    for i in range(n):
        if order[arr[i]] != i:
            index.add(i)
    
    while index:
        idx = next(iter(index))
        s = arr[idx]
        arr[idx], arr[order[s]] = arr[order[s]], arr[idx]


        if arr[idx] == alphabet[idx]:
            index.remove(idx)
        if arr[order[s]] == alphabet[order[s]]:
            index.remove(order[s])

        answer += 1 
        # print(arr)

    print(answer)