#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Add Digits https://leetcode.com/problems/add-digits/
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.  For example:
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
'''

# Solution1: loop
def turnNumAsList(num):
    tmpStr = str(num)
    i = 0
    retList = []
    for i in range(0,len(tmpStr)):
        retList.append(int(tmpStr[i]))
        i += 1
    return retList

def addDigitLoop(num):
    tmpNum = num 

    while tmpNum >= 9:
        tmpNum = sum(turnNumAsList(tmpNum))

    return tmpNum

# Solution2: recursive
def addDigitRecursive(num):
    if num <= 9:
        return num
    tmpList = turnNumAsList(num)
    return addDigitRecursive(sum(tmpList))


# Solution: O(1)
def addDigit(num):
    return num if num <=9 else num % 9
#    if num <= 9:
#        return num
#    else:
#        return num % 9
#

print "8:", addDigitLoop(8)
print "38:", addDigitLoop(38)
print "138:", addDigitLoop(138)

print "8:", addDigitRecursive(8)
print "38:", addDigitRecursive(38)
print "138:", addDigitRecursive(138)

print "8:", addDigit(8)
print "38:", addDigit(38)
print "138:", addDigit(138)
