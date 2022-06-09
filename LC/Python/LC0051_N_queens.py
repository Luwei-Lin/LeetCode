from typing import List

class Solution:
    matrix = []
    
    def isValid(self, tempMatrix:List[str], r: int, c: int):
        #check if the current 'Q' is valid 
        assert len(tempMatrix[0]) > 0
        row, col = len(tempMatrix), len(tempMatrix[0])
        #1.left top corner
        
        for i, j in zip(range(r - 1, -1, -1), range(c - 1, -1, -1)):
            if (i < 0 or j < 0) : break
            if tempMatrix[i][j] == 'Q':
                return False
                
        #2.above rows
        for i in range(r - 1, -1, -1):
            if (i < 0): break
            if tempMatrix[i][c] == 'Q':
                return False
        
        #3. top right corner
        
        for i, j  in zip(range(r - 1, -1, -1), range (c + 1, col)):
            if (i < 0 or j >= col) : break
            if tempMatrix[i][j] == 'Q':
                return False        
        return True
    
    def backtrack(self, tempList:List[str], row):
        if (len(tempList)== row):
            self.matrix.append(tempList.copy())
            return
        
        # another columns. 
        for j in range(len(tempList[0])):
            if(self.isValid(tempList, row, j) is False):
                continue
            #make choice
            tempList[row] = tempList[row][:j] + 'Q' + tempList[row][j+1:]
            #go to the next row to do choices
            self.backtrack(tempList, row + 1)
            #withdraw choice
            tempList[row] = tempList[row][:j] + '.' + tempList[row][j+1:]
    
        
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        #initilize the chess board by input n
        newBoard = []
        for i in range(n):
            row = ""
            for j in range(n):
                row += "."
            newBoard.append(row)
        
        self.backtrack(newBoard, 0)
        
        return self.matrix
        
        
def main():
    s = Solution()
    print(s.solveNQueens(4))
main()