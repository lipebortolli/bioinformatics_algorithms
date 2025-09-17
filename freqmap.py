def frequency_map(text: str, k: int) -> dict:
    """Return the frequency of all k-mers in a DNA string."""
    freq = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        freq[pattern] = freq.get(pattern, 0) + 1
    return freq

def frequent_words(text: str, k: int) -> list:
    """Return the list of most frequent k-mers in a DNA string."""
    freq = frequency_map(text, k)
    max_count = max(freq.values())
    return [pattern for pattern, count in freq.items() if count == max_count]
