from typing import Optional
from typing import List

class Solution:
    res = []
    sum = 0
    def combinationSum3(self, k: int, n: int) :
        self.backtrack(k, n, sum)
        
    def backtrack(self, k, n, sum):
        track = []

        if sum == n:
            self.res.append(track)
        for i in range(0, k):
            track.append(i)
            sum += i
            self.backtrack(k, n, sum)
            track.pop()
            sum -= i
        
def main():
    s = Solution()
    print(s.combinationSum3(3, 7))
main()