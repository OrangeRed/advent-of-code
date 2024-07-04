from typing import Tuple


def getHandType(cards: dict[str, int]) -> int:
    if len(cards) == 1:
        return 6  # Five of a kind
    elif len(cards) == 2 and 4 in cards.values():
        return 5  # Four of a kind
    elif len(cards) == 2 and 3 in cards.values():
        return 4  # Full House
    elif len(cards) == 3 and 3 in cards.values():
        return 3  # Three of a kind
    elif len(cards) == 3 and 2 in cards.values():
        return 2  # Two Pair
    elif len(cards) == 4 and 2 in cards.values():
        return 1  # One Pair
    else:
        return 0  # High Card


value = "23456789TJQKA"
sorted_hands: list[list[Tuple[str, str]]] = [[] for _ in range(0, 7)]
for cards_str, bid in [line.split() for line in open(0).read().splitlines()]:
    cards: dict[str, int] = {}
    for card in cards_str:
        cards[card] = (cards[card] + 1) if card in cards else 1

    hand_type = getHandType(cards)
    insert_at = 0
    for hand, _ in sorted_hands[hand_type]:
        for i, char in enumerate(hand):
            if value.find(cards_str[i]) > value.find(char):
                insert_at += 1
            elif value.find(cards_str[i]) == value.find(char):
                continue  # Try next char pair
            break

    sorted_hands[hand_type].insert(insert_at, (cards_str, bid))


total, rank = 0, 1
for poker_hand in sorted_hands:
    for _, bid in poker_hand:
        total += rank * int(bid)
        rank += 1

print(total)
