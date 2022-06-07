from typing import List

class Solution:
    matrix = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        for i in range(n):
            row = "."
            for j in range(n):
                row += '.'
            self.matrix.append(row)
        print(self.matrix)
        
        
def main():
    s = Solution()
    s.solveNQueens(3)
main()