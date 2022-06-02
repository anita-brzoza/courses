"""
------------------------------------------------------------------------------------------------
The function that transcribed DNA into RNA.
------------------------------------------------------------------------------------------------
"""

def DNA_into_RNA(DNA_sequence):
    RNA_sequence = DNA_sequence.upper().replace("T", "U")
    return RNA_sequence


"""
------------------------------------------------------------------------------------------------
The unit test
------------------------------------------------------------------------------------------------
"""

import unittest
class Test(unittest.TestCase):
    def test_DNA_sequence(self):
        DNA_sequence = "GATGGAACTTGACTACGTAAATT"
        RNA_sequence = DNA_into_RNA(DNA_sequence)
        self.assertEqual(RNA_sequence, "GAUGGAACUUGACUACGUAAAUU")

if __name__ == '__main__':
    unittest.main()