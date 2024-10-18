from collections import Counter
from functools import cmp_to_key

filename = "inputs/day7"

def transform_element(element):
    mapping = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    return int(mapping.get(element, element))

def hand_to_list_of_int(hand):
    return [transform_element(item) for item in list(hand)]

def get_score(hand):
    hand_list = hand_to_list_of_int(hand)
    result = Counter(hand_list)

    if len(set(hand_list)) == 1:
        return 1000
    counts_most_common = result.most_common(1)[0][1]

    if counts_most_common == 4:
        return 900
    if len(set(hand_list)) == 2 and counts_most_common != 4:
        return 800
    if len(set(hand_list)) == 3 and counts_most_common == 3:
        return 700
    if len(set(hand_list)) == 3 and counts_most_common != 3:
        return 600
    if len(set(hand_list)) == 4:
        return 500
    if len(set(hand_list)) == 5:
        return 400
    return 0

def get_second_score(hand):
    score = 0
    for i, number in enumerate(hand_to_list_of_int(hand)):
        score += (10**(12-2*i)) * number
    return score

def custom_compare(hand_x, hand_y):
    hand_x_score = get_score(hand_x)
    hand_y_score = get_score(hand_y)

    if hand_x_score == hand_y_score:
        hand_x_score = get_second_score(hand_x)
        hand_y_score = get_second_score(hand_y)

    return (hand_x_score > hand_y_score) - (hand_x_score < hand_y_score)

lines = open(filename, 'r').readlines()
hand_str_list = [line.split()[0] for line in lines]
dict_machine = {line.split()[0]: int(line.split()[1]) for line in lines}

sorted_hands = sorted(hand_str_list, key=cmp_to_key(custom_compare))

total_winnings = sum(dict_machine[hand] * (idx + 1) for idx, hand in enumerate(sorted_hands))
print(total_winnings)
