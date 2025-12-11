# dnaops – Simple DNA Utility Library

This is a simple Python module that performs common DNA sequence operations
such as length, GC content, reverse complement, motif search, and more.
The code uses a class-based design so that the DNA sequence is stored inside
a 'DNAOps' object, which keeps things clean and easy to reuse.

# Installation

1. Download or clone this project folder to your system.
2. Open a terminal and go to the project root.
3. Install pytest (for running tests): pip install pytest
4. From the project root folder, run: PYTHONPATH=. pytest tests/test_dnaops.py -v
   This runs all unit tests for the 'DNAOps' class that i have given in test_dnaops.py
   and shows "passed" in green.

# Implemented functions (methods of DNAOps)

## Basic sequence checks
- 'length()' – Return length of the DNA sequence.
- 'count_nucleotides()' – Count A, T, G, C separately.
- 'count_ambiguous_bases()' – Count characters not in ATGCN.
- 'validate_dna()' – Check if all bases are in ATGCN (True/False).
- 'replace_invalid_characters_with_n()' – Replace invalid bases with 'N'.
- 'count_purines()' – Count A + G.
- 'count_pyrimidines()' – Count T + C.

## Transformations
- 'generate_complement()' – Complement sequence (A↔T, G↔C).
- 'generate_reverse()' – Reverse the sequence.
- 'generate_reverse_complement()' – Reverse complement.
- 'convert_to_uppercase_and_standardize()' – Uppercase and map invalid bases to 'N'.
- 'replace_characters(mapping_dict)' – Replace bases using a custom mapping.

## Sequence analysis
- 'calculate_gc()' – GC content (%) of full sequence.
- 'calculate_at()' – AT content (%) of full sequence.
- 'calculate_gc_region(start, end)' – GC content (%) for a region.
- 'check_palindrome()' – Check if sequence equals its reverse complement.
- 'nucleotide_dictionary()' – Dictionary of A/T/G/C/N counts.
- 'format_percentage_report()' – Percentage of each base.

## Additional features
- 'find_first_occurrence(motif)' – First index of a motif, or -1.
- 'find_all_positions(motif)' – List of all positions of a motif.
- 'kmer_breakdown(k)' – Counts of all k-mers.
- 'detect_repeats()' – Detect adjacent repeat bases (True/False).
- 'longest_run()' – Longest continuous run of the same base.
- 'transcribe()' – DNA to RNA (T → U).


Renjima Sherin K
11 December 2025

