
from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        res = [0 for i in range(len(nums))]
        for i in range(0, len(nums)):
            if i == 0:
                res[i] = nums[i]
            else:   
                res[i] = nums[i] + res[i - 1]
        print(res)
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    s = Solution()
    s.runningSum(nums)
    
    