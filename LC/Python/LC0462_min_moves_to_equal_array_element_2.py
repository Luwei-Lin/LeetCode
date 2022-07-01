from typing import List
class Solution:
    #not work for [1,0,0,8,6]
    def minMoves2_version1(self, nums: List[int]) -> int:
        sum = 0
        for n in nums:
            sum += n
        average = int(sum / len(nums))
        moves = 0
        for n in nums:
            moves += abs(n - average)
        return moves

    def minMoves2_version2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        mid = nums[int(len(nums)/2)]
        moves = 0
        for n in nums:
            moves += abs(n - mid)
        return moves
        
def main():
    s = Solution()
    print(s.minMoves2_version2([1,2,3]))
main()
