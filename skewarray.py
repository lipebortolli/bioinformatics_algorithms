def skew_array(genome: str) -> list:
    """Return the skew array: cumulative (G-C) difference at each position."""
    skew = [0]
    for nucleotide in genome:
        if nucleotide == 'G':
            skew.append(skew[-1] + 1)
        elif nucleotide == 'C':
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])
    return skew
