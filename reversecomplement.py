from reverse import reverse

def complement(pattern: str) -> str:
    """Return the complement of a DNA string."""
    mapping = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(mapping[nuc] for nuc in pattern)

def reverse_complement(pattern: str) -> str:
    """Return the reverse complement of a DNA string."""
    return reverse(complement(pattern))
