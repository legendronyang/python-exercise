#!//usr/bin/python
# -*- coding: utf-8 -*-

'''
Nim Game https://leetcode.com/problems/nim-game/
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.  Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.  For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.  1次可以移除1到3块石头，你先移，移最后一块石头者为优胜者

解法：找到石头的数目和输赢的联系；如石头数是4的整数倍，先移者必输；返回值为bool （true or false）

解法1:
        if n%4 == 0:
                    return False
                            else:
                                        return True

                                        解法2: return bool(n%4)
                                        解法3: return False if n%4 ==0 else True (三元符的替代: pythonic写法：http://wuzhiwei.net/be_pythonic/）
'''

#Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.  For example:
#Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

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
# Solution: recursive

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
