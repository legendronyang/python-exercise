#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
36. Valid Sudoku   https://leetcode.com/problems/valid-sudoku/
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
'''
import pdb

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        col, retVal = [], True
        for i in range(0,9):
            eachcol = ''
            for j in range(0,9):  
                eachcol += board[j][i]
            col.append(eachcol)   
        for i in range(0,9):
            row, eachcol = board[i], col[i]
            newRow = row.replace('.','')
            newCol = eachcol.replace('.','')
            if len(list(newRow))  != len(set(list(newRow))) or len(list(newCol))  != len(set(list(newCol))):
                retVal = False
                break
        return retVal


#        col, retVal = [], True
#        for i in range(0,8):
#            eachcol = []
#            for j in range(0,8):                 
#                eachcol.append(board[j][i])
#            col.append(eachcol)
#
#        for i in range(0,8):
#            row, eachcol = board[i], col[i]
#            dotRowCount = row.count('.')
#            dotColCount = eachcol.count('.')
#            for k in range(0,dotRowCount):
#                row.remove('.')
#            for k in range(0,dotColCount):
#                eachcol.remove('.')
#            if len(set(row)) != len(row) or len(set(eachcol)) != len(eachcol):
#                retVal = False
#                break
#        
#        return retVal
        
        
                
    def myUnitTest(self,board):
        return Solution.isValidSudoku(self, board)

mySolution = Solution()
mySolution.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])

import unittest

class Test_Solution_myUnitTest(unittest.TestCase):

	def test_myUnitTest(self):
	    self.assertEqual(mySolution.myUnitTest(["...9.....",".........","..3.....1",".........","1.....3..","....2.6..",".9.....7.",".........","8..8....."]), False)
	    self.assertEqual(mySolution.myUnitTest(["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]), True)		
	    self.assertEqual(mySolution.myUnitTest([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]), True)		

#		self.assertEqual(mySolution.myUnitTest([[5,3,'.','.',7,'.','.','.','.'],[6,'.','.',1,9,5,'.','.','.'],['.',9,8,'.','.','.','.',6,'.'],[8,'.','.','.',6,'.','.','.',3],[4,'.','.',8,'.',3,'.','.',1],[7,'.','.','.',2,'.','.','.',6],['.',6,'.','.','.','.',2,8,'.'],['.','.','.',4,1,9,'.','.',5],['.','.','.','.',8,'.','.',7,9]]), True)
#		self.assertEqual(mySolution.myUnitTest([[5,3,'.','.',7,'.','.','.','.'],[5,'.','.',1,9,5,'.','.','.'],['.',9,8,'.','.','.','.',6,'.'],[8,'.','.','.',6,'.','.','.',3],[4,'.','.',8,'.',3,'.','.',1],[7,'.','.','.',2,'.','.','.',6],['.',6,'.','.','.','.',2,8,'.'],['.','.','.',4,1,9,'.','.',5],['.','.','.','.',8,'.','.',7,9]]), False)
#		self.assertEqual(mySolution.myUnitTest([[5,3,'.','.',7,'.','.','.','.'],[6,'.','.',1,9,5,'.','.','.'],['.',9,8,'.','.','.','.',6,'.'],[8,'.','.','.',9,'.','.','.',3],[4,'.','.',8,'.',3,'.','.',1],[7,'.','.','.',2,'.','.','.',6],['.',6,'.','.','.','.',2,8,'.'],['.','.','.',4,1,9,'.','.',5],['.','.','.','.',8,'.','.',7,9]]), False)

												
suite = unittest.TestLoader().loadTestsFromTestCase(Test_Solution_myUnitTest)
unittest.TextTestRunner(verbosity=2).run(suite)