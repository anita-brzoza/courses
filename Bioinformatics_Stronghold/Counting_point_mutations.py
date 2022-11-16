
def hamming_distance(s, t):
    """Calculates the Hamming distance between two sequences of equal length"""

    hamming_distance_count = 0

    for i in range(len(s)):
        if s[i] != t[i]:
            hamming_distance_count += 1
            
    return hamming_distance_count


"""
------------------------------------------------------------------------------------------------
The unit test
------------------------------------------------------------------------------------------------
"""

import unittest
class Test(unittest.TestCase):
    def test_hamming_distance(self):
        s = "GAGCCTACTAACGGGAT"
        t = "CATCGTAATGACGGCCT"
        distance = hamming_distance(s, t)
        self.assertEqual(distance, 7)

if __name__ == '__main__':
    unittest.main()


