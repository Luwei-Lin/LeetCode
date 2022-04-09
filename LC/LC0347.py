
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


def main():
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3,3, 4, 4, 4,4 ]
    res = []
    k = 4
    res = Solution().topKFrequent(nums, k)
    print(res)
    
main()