#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
67. Add Binary   https://leetcode.com/problems/add-binary/
Given two binary strings, return their sum (also a binary string).
For example, a = "11"  b = "1"    Return "100". 
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            b = '0' *(max(len(a),len(b)) - min(len(a),len(b))) + b
        else:  
            a = '0' *(max(len(a),len(b)) - min(len(a),len(b))) + a

        aList, bList = list(a), list(b)
        carryBit, rList = 0, []
        posBit = -1
        while abs(posBit) <= len(aList):
            bitSum = int(aList[posBit]) + int(bList[posBit]) + carryBit
            if bitSum == 3:
                rList.append('1')
                carryBit = 1
            elif bitSum == 2:
                rList.append('0')
                carryBit = 1
            elif bitSum == 1:
                rList.append('1')
                carryBit = 0
            elif bitSum == 0:
                rList.append('0')
                carryBit = 0
            posBit = posBit - 1
        if carryBit == 1:
            rList.append('1')
        rList.reverse()
        rStr = ''
        for i in rList:
            rStr += i
        return rStr 
        
    def myUnitTest(self, a, b):
        return Solution.addBinary(self, a, b)

mySolution = Solution()
mySolution.myUnitTest("11","1")

import unittest
class Test_Solution_myUnitTest(unittest.TestCase):
    def test_myUnitTest(self):
        self.assertEqual(mySolution.myUnitTest("11","1"), "100")
        self.assertEqual(mySolution.myUnitTest("11","11"), "110")
        self.assertEqual(mySolution.myUnitTest("100","10"), "110")        
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_myUnitTest)
unittest.TextTestRunner(verbosity=2).run(suite)     
