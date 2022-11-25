
def finding_motif_in_DNA(s, t):
    """ Function that return all locations of sequence t as a substring of sequence s """

    lenght_sequence = len(s)
    lenght_substring = len(t)

    locations = []

    for nucleotide_index in range(0, lenght_sequence):
        if t[0] == s[nucleotide_index]:
            if t[0: lenght_substring] == s[nucleotide_index : (nucleotide_index + lenght_substring)]:
                locations.append(nucleotide_index + 1)

    return locations

# ------------------------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):
    
    def test_finding_motif_in_DNA(self):
        """Unit test for finding_motif_in_DNA() function"""
        locations = finding_motif_in_DNA("GATATATGCATATACTT", "ATAT")
        self.assertEqual(locations, [2, 4, 10])

if __name__ == '__main__':
    unittest.main()
