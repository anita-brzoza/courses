def rabbits_and_reccurrence_relations(n, k):
    """
    A function that return the total number of rabbits that will be present after n months, 
    if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits 
    produces a litter of k rabbit pairs (instead of only 1 pair).

    Inputs are positive integers n=<40 and k=<5
    """
    rabbits = [0,1] # number of rabbits each month

    for i in range(2,n+1):
        # adding number of rabbits in i-th month
        i_rabbits = rabbits[i-1]+(rabbits[i-2]*k)
        rabbits.append(i_rabbits)

    N_rabbits = rabbits[n] # or rabbits[-1]

    return(N_rabbits)


"""
------------------------------------------------------------------------------------------------
The unit tests
------------------------------------------------------------------------------------------------
"""

import unittest
class Test(unittest.TestCase):
    def test_rabbits_and_reccurrence_relations(self):
        N_rabbits = rabbits_and_reccurrence_relations(5,3)
        self.assertEqual(N_rabbits, 19)

    def test_rabbits_and_reccurrence_relations2(self):
        N_rabbits = rabbits_and_reccurrence_relations(29,3)
        self.assertEqual(N_rabbits, 8878212019)
        
if __name__ == '__main__':
    unittest.main()