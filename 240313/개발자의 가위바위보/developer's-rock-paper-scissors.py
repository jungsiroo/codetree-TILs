import sys
input = sys.stdin.readline

def make_comb(arr,cnt):
    global comb, visited
    if cnt == 3:
        comb.append(arr)
        return

    for i in range(3):
        if visited[i]:
            continue
        visited[i] = True
        make_comb(arr+[use[i]], cnt+1)
        visited[i] = False


if __name__ == "__main__":
    global comb, visited
    comb = []

    use = [1,2,3]
    visited = [False]*3
    make_comb([], 0)

    rounds = []
    n = int(input())

    for _ in range(n):
        player1, player2 = map(int, input().split())
        if player1 == player2:
            continue
        rounds.append([player1, player2])

    answer = 0
    for sissor, paper, rock in comb:
        count = 0 
        for p1, p2 in rounds:
            if (p1 == sissor and p2 == paper) or (p1 == paper and p2 == rock) or (p1==rock and p2 == sissor):
                count += 1
        answer = max(answer, count)

    print(answer)