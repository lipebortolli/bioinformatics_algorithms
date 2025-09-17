# Bioinformatics Algorithms

This repository contains Python implementations of classic bioinformatics algorithms. It is organized for learning, demonstration, and portfolio purposes. Each algorithm is modular, with example scripts and unit tests.

---

## Project Structure

```
bioinformatics_algorithms/
├── approxmatching.py       # Approximate pattern matching
├── freqmap.py              # k-mer frequency and most frequent patterns
├── hammingdistance.py      # Hamming distance calculation
├── patterncount.py         # Count occurrences of a pattern in a sequence
├── patternmatching.py      # Find all occurrences of a pattern in a genome
├── reverse.py              # Reverse a DNA string
├── reversecomplement.py    # Complement and reverse complement of DNA
├── skewarray.py            # Skew array (G-C difference along a genome)
├── symbolarray.py          # Symbol array and faster symbol array
├── README.md               # Project overview
└── LICENSE                 # License (MIT)
```

---

## Implemented Algorithms

- **k-mer Frequency** (`freqmap.py`)  
  Compute frequency of all k-mers and find the most frequent patterns.  

- **Reverse DNA** (`reverse.py`)  
  Reverse a DNA string.  

- **Complement & Reverse Complement** (`reversecomplement.py`)  
  Compute the complement and reverse complement of DNA.  

- **Pattern Matching** (`patternmatching.py`)  
  Find all occurrences of a pattern in a genome.  

- **Pattern Counting** (`patterncount.py`)  
  Count occurrences of a pattern in a sequence.  

- **Symbol Array & Faster Symbol Array** (`symbolarray.py`)  
  Compute counts of a symbol in sliding windows of a genome.  

- **Skew Array** (`skewarray.py`)  
  Track cumulative G-C differences along a genome.  

- **Hamming Distance** (`hammingdistance.py`)  
  Calculate mismatches between two DNA strings.  

- **Approximate Pattern Matching** (`approxmatching.py`)  
  Find patterns allowing a maximum number of mismatches.

---

## How to Run

1. Clone the repository:

git clone https://github.com/lipebortolli/bioinformatics_algorithms.git

cd bioinformatics_algorithms

2. Run an example script (you can create your own in a `examples/` folder):

python freqmap.py

3. Run unit tests (if `pytest` is installed):

pytest tests/

---

## License

This project is licensed under the MIT License.
