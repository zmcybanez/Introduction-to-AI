transactions = [
    ['milk','bread','eggs'],
    ['milk','bread'],
    ['milk','eggs'],
    ['bread','eggs']
]

from collections import Counter

item_count = Counter()

for t in transactions:
    for item in t:
        item_count[item] += 1

print(item_count)