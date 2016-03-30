#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
231. Power of Two   https://leetcode.com/problems/power-of-two/
Given an integer, write a function to determine if it is a power of two. 
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if str(bin(n)).count('1') == 1 and str(bin(n)).count('-') == 0:
            return True
        else:
            return False

    def isPowerOfTwo_On2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        retVal = False
        if (n < 0):
            return retVal
        i = 0
        while True:
            if n == (2 ** i):
                retVal = True
            elif n < (2 ** i):
                break
            i += 1
        return retVal         
        
    def myUnitTest(self,n):
        return Solution.isPowerOfTwo(self, n)

mySolution = Solution()

import unittest

class Test_Solution_myUnitTest(unittest.TestCase):

	def test_titleToNumber(self):
		self.assertEqual(mySolution.myUnitTest(4), True)
		self.assertEqual(mySolution.myUnitTest(5), False)
		self.assertEqual(mySolution.myUnitTest(2 ** 100000000), True)
		self.assertEqual(mySolution.myUnitTest(2 ** 100000000 + 1), False)
										
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_myUnitTest)
unittest.TextTestRunner(verbosity=2).run(suite)
