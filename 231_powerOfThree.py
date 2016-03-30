#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
231. Power of Three   https://leetcode.com/problems/power-of-three/
Given an integer, write a function to determine if it is a power of three.
Follow up:
Could you do it without using any loop / recursion? 
'''

class Solution(object):
    def isPowerOfThree_loop(self, n):
        """
        :type n: int
        :rtype: bool
        """
        retVal = False
        if n < 1:
            return retVal
        i = 0
        while True:
            if n == (3 ** i):
                retVal = True
                break
            elif n < ( 3 ** i):
                break
            i += 1
        return retVal    

    def isPowerOfThree(self, n):  #best answer
        if n <= 0:
            return False

        while n % 3 == 0:           
            n = n / 3

        return True if n == 1 else False
        
    def isPowerOfThree_recursion(self, n):
        """
        :type n: int
        :rtype: bool
        """      
        if n < 1:
            return False
        if n == 1 or n == 3:
            return True
        if n / 3 * 3 == n:
            return Solution.isPowerOfThree(self, n / 3)
        else:
            return False
                
    def myUnitTest(self,n):
        return Solution.isPowerOfThree(self, n)

mySolution = Solution()

import unittest

class Test_Solution_myUnitTest(unittest.TestCase):

	def test_myUnitTest(self):
		self.assertEqual(mySolution.myUnitTest(9), True)
		self.assertEqual(mySolution.myUnitTest(8), False)
		self.assertEqual(mySolution.myUnitTest(3 ** 100), True)
		self.assertEqual(mySolution.myUnitTest(3 ** 10 + 1), False)
										
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_myUnitTest)
unittest.TextTestRunner(verbosity=2).run(suite)
