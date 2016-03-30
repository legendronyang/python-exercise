#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
168. Excel Sheet Column Title   https://leetcode.com/problems/excel-sheet-column-title/
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example: 1 -> A ;   26 -> Z ; 27 -> AA ; 52 -> AZ; 53 -> BA
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        #注意26的边界条件
        #   case 1: 26的整数被
        #   case 2: 其他数
        rStr = ''
        while True:
            if n%26 == 0:
                rStr += 'Z'  
                n = n / 26 - 1  
            else:
                rStr += chr(ord('A') + n%26 -1)
                n = n / 26
            if n <= 0:
                break
            
        return rStr[::-1] 
        
        
    def myUnitTest(self,n):
        return Solution.convertToTitle(self, n)

mySolution = Solution()

import unittest

class Test_Solution_myUnitTest(unittest.TestCase):

	def test_myUnitTest(self):
		self.assertEqual(mySolution.myUnitTest(1), 'A')
		self.assertEqual(mySolution.myUnitTest(26), 'Z')		
		self.assertEqual(mySolution.myUnitTest(27), 'AA')
		self.assertEqual(mySolution.myUnitTest(52), 'AZ')
												
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_myUnitTest)
unittest.TextTestRunner(verbosity=2).run(suite)