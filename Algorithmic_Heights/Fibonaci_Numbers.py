def fibonaci_number(n):
    """
    The functtion to generate value of n Fibonaci number. 
    """
    fib_numb = [0,1] # fibbonaci numbers list

    for i in range(2,n+1):
        # adding next numbers
        i_numb = fib_numb[i-1]+fib_numb[i-2]
        fib_numb.append(i_numb)

    F_n = fib_numb[n] # or fib_numb[-1]

    return(F_n)


"""
------------------------------------------------------------------------------------------------
The unit tests
------------------------------------------------------------------------------------------------
"""

import unittest
class Test(unittest.TestCase):
    def test_fibonaci_number(self):
        F_n = fibonaci_number(0)
        self.assertEqual(F_n, 0)

    def test_fibonaci_number1(self):
        F_n = fibonaci_number(1)
        self.assertEqual(F_n, 1)

    def test_fibonaci_number2(self):
        F_n = fibonaci_number(2)
        self.assertEqual(F_n, 1)
        
    def test_fibonaci_number20(self):
        F_n = fibonaci_number(20)
        self.assertEqual(F_n, 6765)

if __name__ == '__main__':
    unittest.main()