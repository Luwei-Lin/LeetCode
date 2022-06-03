from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[i][j] = matrix[j][i]
        return res
        
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6]]
    s = Solution()
    print(s.transpose(matrix))