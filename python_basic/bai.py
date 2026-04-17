# Pattern 1: Frequency counting
def count_frequency(items):
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Pattern 2: Index mapping (like Two Sum)
def create_index_map(items):
    index_map = {}
    for i, item in enumerate(items):
        index_map[item] = i
    return index_map

# Pattern 3: Default values
from collections import defaultdict
def group_items(items):
    grouped = defaultdict(list)
    for category, value in items:
        grouped[category].append(value)
    return grouped