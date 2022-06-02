"""
------------------------------------------------------------------------------------------------
The function that outputs the reverse complement of the given DNA sequence.
------------------------------------------------------------------------------------------------
"""

def reverse_complement(DNA_sequence):
    nucleotides = {"A":"T", "T":"A", "G":"C", "C":"G"}
    return ''.join([nucleotides[base] for base in DNA_sequence[::-1]])


"""
------------------------------------------------------------------------------------------------
The unit test
------------------------------------------------------------------------------------------------
"""
"""
import unittest
class Test(unittest.TestCase):
    def test_DNA_sequence(self):
        DNA_sequence = "AAAACCCGGT"
        reverse_complement_sequence = reverse_complement(DNA_sequence)
        self.assertEqual(reverse_complement_sequence, "ACCGGGTTTT")

if __name__ == '__main__':
    unittest.main()"""