#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
242. Valid Anagram  https://leetcode.com/problems/valid-anagram/
Given two strings s and t, write a function to determine if t is an anagram of s.
For example,
 	s = "anagram", t = "nagaram", return true.
	s = "rat", t = "car", return false.
Note:
	You may assume the string contains only lowercase alphabets.

'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sList , tList = list(s) , list(t)
        # tList = list(t)
        sList.sort()
        tList.sort()
        if sList == tList:
            return True
        else:
            return False
            
            
mySolution = Solution()

import unittest

class Test_Solution_isAnagram(unittest.TestCase):

	def test_isAnagram_True(self):
		self.assertTrue(mySolution.isAnagram("anagram", "nagaram"), True)
		self.assertTrue(mySolution.isAnagram("b", "b"), True)
		self.assertTrue(mySolution.isAnagram("bbaa", "aabb"), True)
		
	def test_isAnagram_False(self):
		self.assertFalse(mySolution.isAnagram("rat", "car"), False)
 		self.assertFalse(mySolution.isAnagram("anagram", "nagam"), False)
 		self.assertFalse(mySolution.isAnagram("a", "x"), False)

suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_isAnagram)
unittest.TextTestRunner(verbosity=2).run(suite)            
