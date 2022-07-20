from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        assert numRows != 0
        res = [[1]]
        if numRows == 1:
            return res
        
        for i in range(1, numRows):
            previous_row = res[i - 1]
            temp = [1]
            
            for j in range(0, len(previous_row) - 1):
                temp.append ( previous_row[j + 1] + previous_row[j])
            
            temp.append(1)
            res.append(temp)
            
        return res
        
def main():
    s = Solution()
    print(s.generate(5))
main()
