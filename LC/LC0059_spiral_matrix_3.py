class Solution:
    def generateMatrix(self, n: int):
        res = [[0 for i in range(n)] for j in range(n)]
        row = 0
        col = 0
        d = 0
        #four directions right, down, left, up
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        count = 1
        for i in range (n * n):
            res[row][col] = count
            count += 1
            r = (row + dir[d][0]) % n
            c = (col + dir[d][1]) % n
            if res[r][c] != 0:
                d = (d + 1) %4
            
            row += dir[d][0]
            col += dir[d][1]
            
            
                
            
        
        return res
def main():
    n = 3
    print(Solution().generateMatrix(n))
main()