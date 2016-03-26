#!/usr/bin/python
# -*- coding: utf-8 -*- 
'''
Two Sum: https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0,1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    break
            if nums[i] + nums[j] == target:
                break

        return [i,j]

mySolution = Solution()

import unittest

class TestSolution_twoSum(unittest.TestCase):
	def test_twoSum(self):
		self.assertTrue(mySolution.twoSum([3,2,4],6), [1,2])
		self.assertTrue(mySolution.twoSum([3,2,4],7), [0,2])

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution_twoSum)
unittest.TextTestRunner(verbosity=2).run(suite)