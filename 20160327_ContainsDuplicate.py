#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
217. Contains Duplicate   https://leetcode.com/problems/contains-duplicate/
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct. 
'''

class Solution_first(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        retVal = False
        for i in range(len(nums)):
		try:
			for j in range(i+1, len(nums)):
				if nums[j] == nums[i]:
					retVal = True
					raise StopIteration
		except StopIteration:
			break
		
        return retVal

mySolution = Solution()

import unittest

class Test_Solution_containsDuplicate(unittest.TestCase):

	def test_contrainsDuplicate_True(self):
		self.assertTrue(mySolution.containsDuplicate([1,2,2]), True)
		
	def test_contrainsDuplicate_False(self):
		self.assertFalse(mySolution.containsDuplicate([1,2,3]), False)
 		self.assertFalse(mySolution.containsDuplicate([1,5,6,7,8,9]), False)

suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_containsDuplicate)
unittest.TextTestRunner(verbosity=2).run(suite)