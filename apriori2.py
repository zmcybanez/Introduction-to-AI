import itertools
from collections import Counter

# Sample transaction dataset
transactions = [
    ['milk', 'bread', 'eggs'],
    ['milk', 'bread'],
    ['milk', 'eggs'],
    ['bread', 'eggs'],
    ['milk', 'bread', 'butter']
]

pairs = Counter()

for t in transactions:
    for pair in itertools.combinations(t, 2):
        pairs[pair] += 1

print(pairs)