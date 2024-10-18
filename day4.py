import re

# Read data from file and extract card information
cards = [
    {
        "card_number": int(m[0]),
        "matches": len(set(map(int, m[1].split())).intersection(set(map(int, m[2].split()))))
    }
    for m in re.compile(r"Card\s+(\d+):\s*([\d\s]+)\|\s*([\d\s]+)").findall(open("inputs/day4").read())
]

# Calculate the total score
total_score = sum([2 ** (card["matches"] - 1) if card["matches"] > 0 else 0 for card in cards])

# Extend winning tickets
for _, card in enumerate(cards):
    cards.extend(cards[card["card_number"]:card["card_number"] + card["matches"]])

print("Total Score:", total_score)
print("Total Scratchcards", len(cards))
