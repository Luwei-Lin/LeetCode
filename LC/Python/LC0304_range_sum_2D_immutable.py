from typing import List
class NumMatrix:
    preMatrix = [[]]
    def __init__(self, matrix: List[List[int]]):
        r, c = len(matrix), len(matrix[0])
        self.preMatrix = [[0 for i in range(c + 1)] for j in range(r + 1)]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                self.preMatrix[i][j] = self.preMatrix[i - 1][j] + matrix[i - 1][j - 1] + self.preMatrix[i][j - 1] - self.preMatrix[i - 1][j - 1]
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        return self.preMatrix[row2 + 1][col2 + 1] - self.preMatrix[row1][col2 + 1] - self.preMatrix[row2 + 1][col1] + self.preMatrix[row1][col1]

def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    obj = NumMatrix(matrix)
    s = obj.sumRegion(0, 0, 1, 1)
    print(obj.preMatrix)

main()