from patterncount import pattern_count

def symbol_array(genome: str, symbol: str) -> dict:
    """Compute a symbol array counting occurrences of symbol in sliding windows."""
    array = {}
    n = len(genome)
    extended = genome + genome[:n // 2]
    for i in range(n):
        array[i] = pattern_count(extended[i:i + n//2], symbol)
    return array

def faster_symbol_array(genome: str, symbol: str) -> dict:
    """Optimized version of symbol_array using incremental updates."""
    array = {}
    n = len(genome)
    extended = genome + genome[:n//2]
    array[0] = pattern_count(genome[:n//2], symbol)
    for i in range(1, n):
        array[i] = array[i-1]
        if extended[i-1] == symbol:
            array[i] -= 1
        if extended[i + n//2 - 1] == symbol:
            array[i] += 1
    return array
