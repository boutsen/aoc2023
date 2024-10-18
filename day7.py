from functools import cmp_to_key

hands = [(line.split()[0], int(line.split()[1])) for line in open("inputs/day7", 'r').read().splitlines()]

def card_value(card):
    return {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}[card]

def compare_hands(hand1, hand2):
    if hand1 == hand2:
        return 0

    def get_type(hand):
        card_count = sorted([(hand.count(card), card) for card in set(hand)], reverse=True)
        if card_count[0][0] == 5:
            return (1, [card_value(card_count[0][1])])  # Five of a kind
        elif card_count[0][0] == 4:
            return (2, [card_value(card_count[0][1]), card_value(card_count[1][1])])  # Four of a kind
        elif card_count[0][0] == 3 and card_count[1][0] == 2:
            return (3, [card_value(card_count[0][1]), card_value(card_count[1][1])])  # Full house
        elif card_count[0][0] == 3:
            return (4, [card_value(card_count[0][1]), card_value(card_count[1][1]), card_value(card_count[2][1])])  # Three of a kind
        elif card_count[0][0] == 2 and card_count[1][0] == 2:
            return (5, [card_value(card_count[0][1]), card_value(card_count[1][1]), card_value(card_count[2][1])])  # Two pair
        elif card_count[0][0] == 2:
            return (6, [card_value(card_count[0][1]), card_value(card_count[1][1]), card_value(card_count[2][1]), card_value(card_count[3][1])])  # One pair
        else:
            return (7, [card_value(card_count[0][1]), card_value(card_count[1][1]), card_value(card_count[2][1]), card_value(card_count[3][1]), card_value(card_count[4][1])])  # High card

    type1, values1 = get_type(hand1[0])
    type2, values2 = get_type(hand2[0])

    if type1 != type2:
        return -1 if type1 < type2 else 1

    for i in range(len(values1)):
        if values1[i] != values2[i]:
            return -1 if values1[i] >= values2[i] else 1

    return 0

# Sorting the hands based on the rules
sorted_hands = sorted(hands, key=cmp_to_key(compare_hands), reverse=True)

for hand in sorted_hands:
    print(hand)
# Calculate total winnings
print("Total Winnings:", sum(bid * (idx + 1) for idx, (_, bid) in enumerate(sorted_hands)))