from dnaops import DNAOps

def test_length():
    obj = DNAOps("ATGC")
    assert obj.length() == 4

def test_reverse_complement():
    obj = DNAOps("ATGC")
    assert obj.generate_reverse_complement() == "GCAT"

def test_gc_content():
    obj = DNAOps("GCGC")
    assert obj.calculate_gc() == 100.0

def test_first_motif():
    obj = DNAOps("ATATAT")
    assert obj.find_first_occurrence("AT") == 0

def test_longest_run():
    obj = DNAOps("AAATCGGGGG")
    assert obj.longest_run() == 5
