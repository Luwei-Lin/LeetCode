class Solution:
    #if isLive return true
    def bfs(self, row, col, rows, columns, board):
        dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        neighbours = 0
        for d in dir:
            newRow = row + d[0]
            newCol = col + d[1]
            #check if board[newRow][newCol] is out of bound
            if newRow >= rows or newCol >= columns or newRow < 0 or newCol < 0:
                continue
            if board[newRow][newCol] == 1:
                neighbours += 1
        
        if board[row][col] == 1:
            if neighbours < 2 or neighbours > 3:
                return False
            else:# neighbours >= 2 and neighbours <= 3:
                return True
                
        else: #board[row][col] == 0
            if neighbours == 3:
                return True
            else:
                return False
    def gameOfLife(self, board: list[list[int]]) -> None:
        
        columns = len(board[0])
        rows = len(board)
        new_board = []
        for i in range(rows):
            new_row = []
            for j in range(columns):
                if self.bfs(i, j, rows, columns, board):
                    new_row.append(1)
                else:
                    new_row.append(0)
            new_board.append(new_row)
        
        for i in range (rows):
            for j in range (columns):
                board[i][j] = new_board[i][j]
                
    def gameOfLife2(self, board):
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        rows = len(board)
        cols = len(board[0])
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):

                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:

                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                        live_neighbors += 1

                # Rule 1 or Rule 3        
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # Rule 4
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1
                    
        #T O(MN) S O(1) 
    def gameOfLife3(self, board):
        dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        rows = len(board)
        cols = len(board[0])
        
        
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for neighbour in dir:
                    
                    r = row + neighbour[0]
                    c = col + neighbour[1]
                    
                    if ( r >= 0 and r < rows) and (c >= 0 and c <cols) and abs(board[r][c]) == 1:
                        live_neighbors += 1
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):#rule 1 or 3 
                    board[row][col] = -1
                    #-1 means cell is now dead but originally was live
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2
                    #2 means cell is now live but originally was dead
                
        #get the final representation for the newly updated board
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else :
                    board[row][col] = 0
    
    
def main():
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    #board = [[1,1],[1,0]]
    Solution().gameOfLife3(board)
    print(board)
main()

    