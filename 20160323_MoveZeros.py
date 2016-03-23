#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
283. Move Zeroes  https://leetcode.com/problems/move-zeroes/
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
Note:
   You must do this in-place without making a copy of the array.
   Minimize the total number of operations.
'''


class Solution(object):
    def moveZeroes(self, nums):
        ''' 
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        ''' 
        j = len(nums)
        i = 0
        while i < j :
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(len(nums)+1, 0)
                j = j - 1
            else:
                i = i + 1
        print "numbers:", nums
        return    


mySolution = Solution()
mySolution.moveZeroes([0,0,1])
