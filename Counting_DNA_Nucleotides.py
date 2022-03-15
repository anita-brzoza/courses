"""
------------------------------------------------------------------------------------------------
The function that counts the nucleotides present in the given DNA sequence.
Output is a list containing the nuber of nucleotides of adenine, cytosine, guanine and thymine.
------------------------------------------------------------------------------------------------
"""

def count_nucleotides(DNA_sequence):
    return [DNA_sequence.count(n) for n in "ACGT"]


"""
------------------------------------------------------------------------------------------------
The unit test
------------------------------------------------------------------------------------------------
"""

import unittest
class Test(unittest.TestCase):
    def test_DNA_sequence(self):
        DNA_sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        nucleotides = count_nucleotides(DNA_sequence)
        self.assertEqual(nucleotides, [20, 12, 17, 21])

if __name__ == '__main__':
    unittest.main()