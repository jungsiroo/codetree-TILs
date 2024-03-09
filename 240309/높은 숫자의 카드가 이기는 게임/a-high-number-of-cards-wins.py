import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    cards = set([i for i in range(1, 2*n+1)])
    B_cards = []

    for _ in range(n):
        card = int(input())
        cards.remove(card)
        B_cards.append(card)
    
    A_cards = sorted(list(cards))
    B_cards.sort()

    index = 0
    answer = 0

    for b_card in B_cards:
        if index == n:
            break

        if A_cards[index] > b_card:
            answer += 1
        else:
            while A_cards[index]<=b_card:
                if index == n-1:
                    break
                index += 1

            if A_cards[index] > b_card:
                answer += 1
        index += 1
            

    print(answer)