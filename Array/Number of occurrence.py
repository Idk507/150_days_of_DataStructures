from collections import Counter

def countOccurrences(arr, x):
    # Counter creates a frequency dictionary
    freq = Counter(arr)
    return freq[x] if x in freq else 0
