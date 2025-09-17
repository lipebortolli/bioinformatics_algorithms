def pattern_matching(pattern: str, genome: str) -> list:
    """Return all starting positions where pattern appears in genome."""
    positions = []
    len_pattern = len(pattern)
    len_genome = len(genome)
    for i in range(len_genome - len_pattern + 1):
        if genome[i:i + len_pattern] == pattern:
            positions.append(i)
    return positions
