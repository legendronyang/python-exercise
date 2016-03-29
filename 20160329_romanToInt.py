#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
13. Roman to Integer   https://leetcode.com/problems/roman-to-integer/
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
把一个给定的罗马字符转为数字。首先要了解罗马字符表示的规则。
一，羅馬數字共有7個，即I（1）、V（5）、X（10）、L（50）、C（100）、D（500）和M（1000）。
二，在較大的羅馬數字的右邊記上較小的羅馬數字，表示大數字加小數字，例如：VI（6），VIII（8），LV（55=50 + 5），LX（60=50 + 10）
三，在較大的羅馬數字的左邊記上較小的羅馬數字，表示大數字减小數字，例如：IX（9），XL（40=50 - 10），XC（90=100 - 10）
四，左减的数字有限制，仅限于I、X、C。比如45不可以写成VL，只能是XLV。
五，左減時不可跨越一個位數。比如，99不可以用IC（100 - 1）表示，而是用XCIX（[100 - 10] + [10 - 1]）表示。

解题思路，有二条处理逻辑：
一，判断当前字符是否比next字符小，如果小的话需要用下一个字符减去当前字符加到最终结果字符身上。
二，否则的话，就把当前字符直接加到最终结果字符。

'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i, rNum = 0, 0
        while i < len(s) - 1:  #防止字符串S的index out of range
            if romanDict[s[i]] < romanDict[s[i+1]]:
                rNum +=  romanDict[s[i+1]] - romanDict[s[i]]
                i += 2
            else:
                rNum += romanDict[s[i]] 
                i += 1
        if  (len(s) == (i+1)): #覆盖只有一个字符，已经是否最后一位
            rNum += romanDict[s[i]] 
        return rNum       

mySolution = Solution()

import unittest

class Test_Solution_romanToInt(unittest.TestCase):

	def test_romanToInt(self):
		self.assertEqual(mySolution.romanToInt('XCIX'), 99)
		self.assertEqual(mySolution.romanToInt('XLV'), 45)		
		self.assertEqual(mySolution.romanToInt('VIII'), 8)		
		self.assertEqual(mySolution.romanToInt('LV'), 55)	
	
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_romanToInt)
unittest.TextTestRunner(verbosity=2).run(suite)