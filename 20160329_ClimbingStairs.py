#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
70. Climbing Stairs   https://leetcode.com/problems/climbing-stairs/
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top? 

'''

class Solution_best(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if (n == 1 or n == 2):
            return n
        a,b = 1,2
        i = 1
        while i <= n - 2 :
            a,b = b, a+b
            i += 1
        return b
               
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 1 or n == 2):
            return n
   
        return (Solution.climbStairs(self, n-1) + Solution.climbStairs(self, n -2) )

mySolution = Solution()

import unittest

class Test_Solution_climbStairs(unittest.TestCase):

	def test_climbStairs(self):
		self.assertEqual(mySolution.climbStairs(1), 1)
		self.assertEqual(mySolution.climbStairs(3), 3)			
	
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_climbStairs)
unittest.TextTestRunner(verbosity=2).run(suite)