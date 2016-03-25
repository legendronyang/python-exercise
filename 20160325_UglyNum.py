#!/usr/bin/python
# -*- coding: utf-8 -*- 

'''
263. Ugly Number   https://leetcode.com/problems/ugly-number/
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
Note that 1 is typically treated as an ugly number. 
'''

'''
Solution 1: 递归解法
'''
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
		#Base situation 
        if num <= 0:
            return False
        if num == 1 or num == 2 or num == 3 or num == 5:  #可以写成 num in (1,2,3,5)
            return True

		#Recursion
        if num % 2 == 0:
            return Solution.isUgly(self, num / 2)
        elif num % 3 == 0:
            return Solution.isUgly(self, num / 3)        
        elif num % 5 == 0:
            return Solution.isUgly(self, num / 5)
        else:
			return False

'''
Solution 2: 递归解法
'''        
class Solution2(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Base situation
        if num < 1:
            return False
        if num in (1,2,3,5):
            return True
        # Recursion
        q5, r5 = divmod(num,5)  #返回商与余数的元组  http://www.ahlinux.com/python/9668.html
        if r5 == 0:
            return self.isUgly(q5)
        else:
            q3, r3 = divmod(num,3)
            if r3 == 0:
                return self.isUgly(q3)
            else:
                q2, r2 = divmod(num , 2)
                if r2 == 0:
                    return self.isUgly(q2)
                else:
                    return False


'''
Solution 3: 循环
'''
class Solution3(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Base situation
        if num < 1:
            return False
        if num in (1,2,3,5):
            return True

        while (num%2 == 0):
			num = num / 2
        while num % 3 == 0:
			num = num / 3
        while num % 5 == 0:
			num = num / 5
		
        if num == 1:
			return True
        else:
			return False

######### unit test cases:
mySolution = Solution3()

import unittest

class TestSolution_isUgly(unittest.TestCase):

  def test_isUgly_true(self):
      self.assertEqual(mySolution.isUgly(1), True)      
      self.assertEqual(mySolution.isUgly(2), True)        
      self.assertEqual(mySolution.isUgly(3), True)      
      self.assertEqual(mySolution.isUgly(4), True)      
      self.assertEqual(mySolution.isUgly(5), True)       

  def test_isUgly_false(self):
      self.assertEqual(mySolution.isUgly(-1234), False)      
      self.assertEqual(mySolution.isUgly(14), False)        
      self.assertEqual(mySolution.isUgly(7), False)      
      self.assertEqual(mySolution.isUgly(4.23), False)      

suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution_isUgly)
unittest.TextTestRunner(verbosity=2).run(suite)