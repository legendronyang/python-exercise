#!/usr/bin/python
# -*- coding: utf-8 -*- 

'''
263. Ugly Number   https://leetcode.com/problems/ugly-number/
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
Note that 1 is typically treated as an ugly number. 
'''

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1 or num == 2 or num == 3 or num == 5:
            return True
        if num % 2 == 0:
            return Solution.isUgly(self, num / 2)
        if num % 3 == 0:
            return Solution.isUgly(self, num / 3)        
        if num % 5 == 0:
            return Solution.isUgly(self, num / 5)
        return False
        

######### unit test cases:
mySolution = Solution()

import unittest

class TestSolution_isUgly(unittest.TestCase):

  def test_isUgly_true(self):
      self.assertEqual(mySolution.isUgly(1), True)      
      self.assertEqual(mySolution.isUgly(2), True)        
      self.assertEqual(mySolution.isUgly(3), True)      
      self.assertEqual(mySolution.isUgly(4), True)      
      self.assertEqual(mySolution.isUgly(5), True)       

  def test_isUgly_false(self):
      self.assertEqual(mySolution.isUgly(-1234), False)      
      self.assertEqual(mySolution.isUgly(14), False)        
      self.assertEqual(mySolution.isUgly(7), False)      
      self.assertEqual(mySolution.isUgly(4.23), False)      

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution_isUgly)
unittest.TextTestRunner(verbosity=2).run(suite)