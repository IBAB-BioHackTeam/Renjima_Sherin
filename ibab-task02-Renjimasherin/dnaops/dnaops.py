"""A simple class for performing DNA sequence operations."""

class DNAOps:
    def __init__(self, seq):
        self.seq = seq.upper()

    """BASIC SEQUENCE OPERATIONS"""

    """Return the length of the DNA sequence."""
    def length(self):
        return len(self.seq)

    """Count each nucleotide (A, T, G, C) separately."""
    def count_nucleotides(self):
        nucleotides = []
        for char in "ATGC":
            seq = self.seq.count(char)
            nucleotides.append(seq)
        return nucleotides

    """Count ambiguous bases (anything not ATGCN)."""
    def count_ambiguous_bases(self):
        nucleotides = "ATGCN"
        sum=0
        for char in self.seq:
            if char not in nucleotides:
                sum+=1
        return sum

    """Validate DNA (valid only if base ∈ A/T/G/C/N) → return True/False"""
    def validate_dna(self):
        return all(char in "ATGCN" for char in self.seq)

    """Replace invalid characters with "N"."""
    def replace_invalid_characters_with_n(self):
        return "".join("N" if char not in "ATGCN" else char for char in self.seq)

    """Return number of purines (A + G)."""
    def count_purines(self):
        return self.seq.count("A") + self.seq.count("G")

    """Return number of pyrimidines (T + C)."""
    def count_pyrimidines(self):
        return self.seq.count("T") + self.seq.count("C")

    """TRANSFORMATIONS"""

    """Generate the complement"""
    def generate_complement(self):
        complement = ""
        for char in self.seq:
            if char == "A":
                complement += "T"
            elif char == "G":
                complement += "C"
            elif char == "C":
                complement += "G"
            elif char == "T":
                complement += "A"
        return complement

    """Generate the reverse"""
    def generate_reverse(self):
        return self.seq[::-1]

    """Generate the reverse complement."""
    def generate_reverse_complement(self):
        complement = self.generate_complement()
        return complement[::-1]

    """Convert the sequence to uppercase and standardize (ATGCN only)."""
    def convert_to_uppercase_and_standardize(self):
        new_seq = ""
        for char in self.seq:
            if char in "ATGC":
                new_seq += char
            else:
                new_seq += "N"
        return new_seq

    """Replace characters using mapping rules (example: A→T or G→C)."""
    def replace_characters(self, mapping_dict):
        new_seq = ""
        for char in self.seq:
            if char in mapping_dict:
                new_seq += mapping_dict[char]
            else:
                new_seq += char
        return new_seq

    """SEQUENCE ANALYSIS"""

    """Calculate GC content (entire sequence)."""
    def calculate_gc(self):
        if not self.seq:
            return 0
        gc = sum(1 for b in self.seq if b in "GC")
        return gc / len(self.seq) * 100

    """Calculate AT content"""
    def calculate_at(self):
        if len(self.seq) == 0:
            return 0
        at = 0
        for i in self.seq:
            if i == "A" or i == "T":
                at += 1
        return at / len(self.seq) * 100

    """Calculate GC content for a user-defined region (start–end)."""

    def calculate_gc_region(self, start, end):
        region = self.seq[start:end]
        if not region:
            return 0.0
        gc = sum(1 for b in region if b in "GC")
        return gc / len(region) * 100

    """Check whether sequence is a palindrome."""
    def check_palindrome(self):
        return self.seq == self.generate_reverse_complement()

    """Return a nucleotide frequency dictionary"""
    def nucleotide_dictionary(self):
        freq = {"A": 0, "T": 0, "G": 0, "C": 0, "N": 0}
        for i in self.seq:
            if i == "A":
                freq["A"] += 1
            elif i == "T":
                freq["T"] += 1
            elif i == "G":
                freq["G"] += 1
            elif i == "C":
                freq["C"] += 1
            elif i == "N":
                freq["N"] += 1
        return freq

    """Generate a formatted percentage report of each base"""
    def format_percentage_report(self):
        total = len(self.seq)
        freq = self.nucleotide_dictionary()
        report = {}
        for key in freq:
            if total == 0:
                report[key] = 0
            else:
                report[key] = (freq[key] / total) * 100
        return report

    """ADDITIONAL FUNCTIONS"""

    """Find the first occurrence of a motif."""
    def find_first_occurrence(self, motif):
        motif = motif.upper()
        m = len(motif)
        for i in range(len(self.seq) - m + 1):
            if self.seq[i:i + m] == motif:
                return i
        return -1

    """Find all positions of a given motif."""
    def find_all_positions(self, motif):
        motif = motif.upper()
        m = len(motif)
        positions = []
        for i in range(len(self.seq) - m + 1):
            if self.seq[i:i + m] == motif:
                positions.append(i)
        return positions

    """Return a k-mer breakdown (user inputs value of k)"""
    def kmer_breakdown(self, k):
        kmers = {}
        for i in range(len(self.seq) - k + 1):
            kmer = self.seq[i:i + k]
            if kmer in kmers:
                kmers[kmer] += 1
            else:
                kmers[kmer] = 1
        return kmers

    """Detect whether the DNA contains repeats (simple detection)."""
    def detect_repeats(self):
        for i in range(len(self.seq) - 1):
            if self.seq[i] == self.seq[i + 1]:
                return True
        return False

    """Identify longest continuous run of a single nucleotide."""
    def longest_run(self):
        if len(self.seq) == 0:
            return 0
        longest = 1
        current = 1
        for i in range(1, len(self.seq)):
            if self.seq[i] == self.seq[i - 1]:
                current += 1
                if current > longest:
                    longest = current
            else:
                current = 1
        return longest

    """Transform DNA to RNA."""

    def transcribe(self):
        rna = ""
        for i in self.seq:
            if i == "A":
                rna += "A"
            elif i == "T":
                rna += "U"
            elif i == "G":
                rna += "G"
            elif i == "C":
                rna += "C"
            elif i == "N":
                rna += "N"
            else:
                rna += "N"
        return rna

