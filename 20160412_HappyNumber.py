#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
202. Happy Number   https://leetcode.com/problems/happy-number/
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

    1**2 + 9**2 = 82
    8**2 + 2**2 = 68
    6**2 + 8**2 = 100
    1**2 + 0**2 + 0**2 = 1
 
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        newNum, coveredNum, retVal = n, [], False
        while True:
            tmpNewNum = 0
            for i in list(str(newNum)):
                tmpNewNum += int(i) ** 2
            if tmpNewNum == 1:
                retVal = True
                break
            elif coveredNum.count(tmpNewNum) == 1:
                retVal = False
                break
            else:
                coveredNum.append(tmpNewNum)
                newNum = tmpNewNum
        return retVal        
        
    def myUnitTest(self, n):
        return Solution.isHappy(self, n)

mySolution = Solution()

import unittest
class Test_Solution_myUnitTest(unittest.TestCase):
    def test_myUnitTest(self):
        self.assertEqual(mySolution.myUnitTest(19), True)
        self.assertEqual(mySolution.myUnitTest(1), True)
        self.assertEqual(mySolution.myUnitTest(2), False)        
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_myUnitTest)
unittest.TextTestRunner(verbosity=2).run(suite)     
