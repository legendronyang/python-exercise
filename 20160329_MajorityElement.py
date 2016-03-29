#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in set(nums):
            if nums.count(i) > len(nums) / 2:
                break
        return i

mySolution = Solution()

import unittest

class Test_Solution_majorityElement(unittest.TestCase):

	def test_majorityElement(self):
		self.assertEqual(mySolution.majorityElement([1,2,3,2,2]), 2)
						
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_majorityElement)
unittest.TextTestRunner(verbosity=2).run(suite)
