#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
165. Compare Version Numbers   https://leetcode.com/problems/compare-version-numbers/
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", 
it is the fifth second-level revision of the second first-level revision.
'''

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        retVal = 0
        ver1, ver2 = version1.split('.'), version2.split('.')
        ver3, ver4 = [], []
        for i in range(max(len(ver1), len(ver2))):
            if i >= len(ver1):
                ver3.append(0)
            else:
                ver3.append(int(ver1[i]))
            if i >= len(ver2):
                ver4.append(0)
            else:
                ver4.append(int(ver2[i]))
            
        for i in range(max(len(ver1), len(ver2))):
            if ver3[i] > ver4[i]:
                retVal = 1
                break
            if ver3[i] < ver4[i]:
                retVal = -1
                break
        return retVal

mySolution = Solution()

import unittest

class Test_Solution_compareVersion(unittest.TestCase):

	def test_compareVersion_1(self):
		self.assertEqual(mySolution.compareVersion('2.0', '1.0'), 1)
		self.assertEqual(mySolution.compareVersion('2.0.5', '1.0'), 1)		
		self.assertEqual(mySolution.compareVersion('2.0.5.6', '2.0.4.5'), 1)		
		self.assertEqual(mySolution.compareVersion('2', '1.0'), 1)	
	
	def test_compareVersion_minus1(self):
		self.assertEqual(mySolution.compareVersion('1.0', '2.0'), -1)
 		self.assertEqual(mySolution.compareVersion('1.0.5','1.1' ), -1)
 		
	def test_compareVersion_0(self):
		self.assertEqual(mySolution.compareVersion('1.0', '1.0'), 0)
		self.assertEqual(mySolution.compareVersion('1.0', '1'), 0)
		self.assertEqual(mySolution.compareVersion('1.1.0', '1.1'), 0)
		self.assertEqual(mySolution.compareVersion('1.1', '1.01.0'), 0)
		
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_compareVersion)
unittest.TextTestRunner(verbosity=2).run(suite)