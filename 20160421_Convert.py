#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
6. ZigZag Conversion   https://leetcode.com/problems/zigzag-conversion/
 
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        elif numRows == 2:
            rStr1, rStr2 = '', ''
            for i in range(len(s)):
                if i%2:
                    rStr2 += s[i]
                else:
                    rStr1 += s[i]
            return rStr1 + rStr2
        else:     
            length, indexList = len(s), []
            for i in range(numRows):
                indexList.append([])
            for i in range(1, length + 1):
                 if i % (2 * numRows - 2) == 0: 
                    indexList[numRows - 1 - 1].append(i)
                 elif i % (2 * numRows - 2) <= numRows :
                    indexList[i % (2 * numRows - 2) - 1].append(i)
                 else:
                    indexList[i % (2 * numRows - 2) - numRows ].append(i)

            newList, rStr = [] , ''
            for i in range(len(indexList)):
                newList += indexList[i]
            
            for i in newList:
                rStr += s[i-1]
            return rStr                    
        
    def myUnitTest(self, s, n):
        return Solution.convert(self, s, n)

mySolution = Solution()
mySolution.convert("PAYPALISHIRING", 3)

import unittest
class Test_Solution_myUnitTest(unittest.TestCase):
    def test_myUnitTest(self):
        self.assertEqual(mySolution.myUnitTest("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(mySolution.myUnitTest("A", 1), "A") 
        self.assertEqual(mySolution.myUnitTest("ABC", 2), "ACB")
        self.assertEqual(mySolution.myUnitTest("ABCDE", 3), "AEBDC")
        self.assertEqual(mySolution.myUnitTest("ABCDE", 4), "ABECD")
                                
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_myUnitTest)
unittest.TextTestRunner(verbosity=2).run(suite)     
