#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
278. First Bad Version   https://leetcode.com/problems/first-bad-version/
 You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API. 
'''

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        latestGood, latestBad = 0, n
        
        while latestBad - latestGood > 1:
            if Solution.isBadVersion(self, (latestGood + latestBad) / 2):
                latestBad = (latestGood + latestBad) / 2
            else:
                latestGood = (latestGood + latestBad) / 2
        return latestBad

    def isBadVersion(self, version):
        if version >= 4:
            return True
        else:
            return False
        
    def myUnitTest(self,n):
        return Solution.firstBadVersion(self, n)

mySolution = Solution()

import unittest

class Test_Solution_myUnitTest(unittest.TestCase):

	def test_myUnitTest(self):
		self.assertEqual(mySolution.myUnitTest(10), 4)
		self.assertEqual(mySolution.myUnitTest(20), 4)
		self.assertEqual(mySolution.myUnitTest(100), 4)
										
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_myUnitTest)
unittest.TextTestRunner(verbosity=2).run(suite)
