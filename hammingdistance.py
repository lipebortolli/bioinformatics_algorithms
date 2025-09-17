def hamming_distance(p: str, q: str) -> int:
    """Return the Hamming distance between two DNA strings."""
    return sum(1 for a, b in zip(p, q) if a != b)
