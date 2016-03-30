#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
66. Plus One   https://leetcode.com/problems/plus-one/
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """ 
        index = -1
        while True:
            if digits[index] == 9:
                if abs(index) == len(digits):
                    digits[index] = 0
                    digits.insert(0,1)
                    break
                else:
                #当前位改为0，继续循环；否则，当前为加1，退出循环
                    digits[index] = 0
                    index = index - 1    
            else:
                digits[index] += 1
                break
        return digits                    
        
    def myUnitTest(self,n):
        return Solution.plusOne(self, n)

mySolution = Solution()

import unittest

class Test_Solution_myUnitTest(unittest.TestCase):

	def test_myUnitTest(self):
		self.assertEqual(mySolution.myUnitTest([1]), [2])
		self.assertEqual(mySolution.myUnitTest([9,9]), [1,0,0])		
		self.assertEqual(mySolution.myUnitTest([1,1,1,1]), [1,1,1,2])
		self.assertEqual(mySolution.myUnitTest([1,1,9,9]), [1,2,0,0])
												
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_myUnitTest)
unittest.TextTestRunner(verbosity=2).run(suite)