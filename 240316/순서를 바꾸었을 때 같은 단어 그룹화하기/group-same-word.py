import sys
from string import ascii_lowercase as LOWER, ascii_uppercase as UPPER
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    groups = dict()

    for _ in range(n):
        cnt = {elem:0 for elem in LOWER+UPPER}

        string = input().strip()
        m = len(string)

        for i in range(m):
            cnt[string[i]] = cnt.get(string[i],0)+1
        
        hash_string = ''
        for key, value in cnt.items():
            hash_string += f"{key}{value}"
        
        groups[hash(hash_string)] = groups.get(hash(hash_string), 0)+1

    answer = sorted(groups.items(), key=lambda x:x[1], reverse=True)[0][1]
    print(answer)