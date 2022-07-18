from typing import List
class Solution:
    #bottom up
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        assert len(cost) != 0
        #minicost 1 element longer than cost[]
        minicost = [0 for i in range(len(cost) + 1)]
        
        for i in range(2, len(cost) + 1):
            minicost[i] = min((minicost[i - 1] + cost[i - 1]), (minicost[i - 2] + cost[i - 2]))
        return minicost[-1]
    
    #bottom down
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        assert len(cost) != 0
        memo = {}
        def minicost(step):
            if step <= 1:
                return 0
            
            if step in memo:
                return memo[step]
                
            c = min((minicost(step - 1) + cost[step - 1]), minicost(step - 2) + cost[step - 2])
            memo[step] = c
            
            return memo[step]
        return minicost(len(cost))
        
def main():
    cost = [1, 3, 2, 5, 6, 10, 4]
    s = Solution()
    print(s.minCostClimbingStairs2(cost))
main()
