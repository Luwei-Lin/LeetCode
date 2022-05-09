class Solution:
    def shiftGrid(self, grid, k):
        res = []
        row = len(grid)
        column = len(grid[0])
        #flat the matrix to 1-D 
        temp = []
        for i in range(0, row):
            for j in range (0, column):
                temp.append(grid[i][j])
        #shift in the 1-D array
        for i in range(0, k):
            t = temp.pop()
            temp.insert(0, t)
        #build new matrix
        for i in range(0, row):
            newRow = []
            for j in range(0, column):
                newRow.append(temp[i * column + j])
            res.append(newRow)
        
        return res

def main():
    #grid = [[1,2,3],[4,5,6],[7,8,9]]
    #k = 1
    grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
    k = 4
    
    print(Solution().shiftGrid(grid, k))
main()