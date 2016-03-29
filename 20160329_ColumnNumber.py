#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
171. Excel Sheet Column Number   https://leetcode.com/problems/excel-sheet-column-number/
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example: A -> 1;   AA-> 27
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        rNum = 0
        for i in range(len(s)):
            rNum += (ord(list(s)[i]) - ord('A') +1 ) * (26 ** (len(s) -1 - i))
        return rNum

mySolution = Solution()

import unittest

class Test_Solution_titleToNumber(unittest.TestCase):

	def test_titleToNumber(self):
		self.assertEqual(mySolution.titleToNumber('A'), 1)
		self.assertEqual(mySolution.titleToNumber('AA'), 27)
		self.assertEqual(mySolution.titleToNumber('Z'), 26)
		self.assertEqual(mySolution.titleToNumber('BA'), 53)
						
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_titleToNumber)
unittest.TextTestRunner(verbosity=2).run(suite)
