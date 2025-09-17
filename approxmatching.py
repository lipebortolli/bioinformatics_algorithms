from hammingdistance import hamming_distance

def approximate_pattern_matching(text: str, pattern: str, d: int) -> list:
    """Return all positions where pattern appears in text with at most d mismatches."""
    positions = []
    k = len(pattern)
    for i in range(len(text) - k + 1):
        if hamming_distance(pattern, text[i:i + k]) <= d:
            positions.append(i)
    return positions

def approximate_pattern_count(pattern: str, text: str, d: int) -> int:
    """Return the number of occurrences of pattern in text with at most d mismatches."""
    count = 0
    k = len(pattern)
    for i in range(len(text) - k + 1):
        if hamming_distance(pattern, text[i:i + k]) <= d:
            count += 1
    return count
