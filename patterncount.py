def pattern_count(pattern: str, text: str) -> int:
    """Return the number of times pattern appears in text."""
    count = 0
    len_pattern = len(pattern)
    len_text = len(text)
    for i in range(len_text - len_pattern + 1):
        if text[i:i + len_pattern] == pattern:
            count += 1
    return count
