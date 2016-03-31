#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
66. Plus One   https://leetcode.com/problems/plus-one/
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.
'''
import sys

class Solution_inPlaceReplace(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """ 
        index = -1
        while True:
            if digits[index] == 9:
                digits[index] = 0
                if abs(index) == len(digits):
                    digits.insert(0,1)
                    break
                else:
                #当前位改为0，继续循环；否则，当前为加1，退出循环
                    index = index - 1    
            else:
                digits[index] += 1
                break
        return digits          
                  
    def myUnitTest(self,n):
        return Solution.plusOne(self, n)
        
class Solution(object): # python: sys.maxint   超过最大值的列表将会导致memory overflow
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 将输入整数列表先拼接成整数，加1后，再变回整数列表 
        digitsStr = ''
        for i in digits:
            digitsStr += str(i)

        return [int(x) for x in list(str(int(digitsStr) + 1))]
                
    def myUnitTest(self,n):
        return Solution.plusOne(self, n)

class Solution_3(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """ 
        #j = 0
        #while True:
        #    if digits[-1] != 9:
        #        digits[-1] += 1
        #        break
        #    else:
        #        digits.pop(-1) 
        #        j += 1                
        #        if not len(digits):
        #            digits.insert(0,1)
        #            break
        #digits.extend([0] * j )
        #return  digits
        j = 0
        while len(digits):
            if digits[-1] != 9:
                digits[-1] += 1
                break
            else:
                j += 1 
                digits.pop(-1) 
                               
        if not len(digits):
            digits.insert(0,1)
        digits.extend([0] * j )
        return  digits


    def myUnitTest(self,n):
        return Solution.plusOne(self, n)

class Solution_best(object): # Best answer
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """ 
        j = 0
        while len(digits):
            if digits[-1] == 9:
                digits.pop(-1) 
                j += 1   
            else:
                digits[-1] += 1
                break
        if not len(digits):
            digits.insert(0,1)
        digits.extend([0] * j )
        return  digits
        
    def myUnitTest(self,n):
        return Solution.plusOne(self, n)

class Solution_4(object): # Answer from Leetcode sharing
    def plusOne(self, digits):
        for i in xrange(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits 
        
    def myUnitTest(self,n):
        return Solution.plusOne(self, n)


















class Solution_wuli(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """ 
        
        n = len(digits)
        v = 0L
        for i in range(n):
            v += digits[i] * 10 ** (n-i-1)

        v+=1
        print "v = %s" % v
        s = str(v)
        lst = list(s)
        lst = [int(x) for x in lst]
        print lst
        return lst
        
    def myUnitTest(self,n):
        return Solution.plusOne(self, n)

 


























                                
mySolution = Solution()

import unittest

class Test_Solution_myUnitTest(unittest.TestCase):

	def test_myUnitTest(self):
		self.assertEqual(mySolution.myUnitTest([1]), [2])
		self.assertEqual(mySolution.myUnitTest([9,9]), [1,0,0])		
		self.assertEqual(mySolution.myUnitTest([1,1,1,1]), [1,1,1,2])
		self.assertEqual(mySolution.myUnitTest([1,1,9,9]), [1,2,0,0])
		self.assertEqual(mySolution.myUnitTest([9, 2, 2, 3, 3, 7, 2, 0, 3, 6, 8, 5, 4, 7, 7, 5, 8, 0, 7]), [ 9, 2, 2, 3, 3, 7, 2, 0, 3, 6, 8, 5, 4, 7, 7, 5, 8, 0, 8])
		self.assertEqual(mySolution.myUnitTest([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]), [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
		self.assertEqual(mySolution.myUnitTest([9,9,9,9,9,9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,9,9,9,9,9,9,9,9,9,9]), [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
																
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_myUnitTest)
unittest.TextTestRunner(verbosity=2).run(suite)
