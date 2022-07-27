from math import ceil
from typing import List
class Solution:
    def rob1(self, nums: List[int]) -> int:
        #naive version only consider odd , even
        
        odd_sum = 0
        even_sum = 0
        for i in range(ceil(len(nums)/2)):
            if 2 * i + 1 <  len(nums) :
                odd_sum += nums[2 * i + 1]
            even_sum += nums[2 * i] 
        return max(odd_sum, even_sum)
class Solution2:
    def __init__(self) -> None:
        self.memo = {}
    def rob(self, nums: List[int])-> int:
        self.memo = {}
        return self.robFrom(0, nums)
    def robFrom(self, i, nums):
        #no more house to exam
        if i >= len(nums):
            return 0
        #return cache value.
        if i in self.memo:
            return self.memo[i]
        #Recursive relation evaluation to get the optimal answer
        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])
        
        self.memo[i] = ans
        return ans
        
def main():
    s = Solution()
    nums = [2, 7, 9, 3, 1]
    s2 = Solution2()
    print(s2.rob(nums))
main()