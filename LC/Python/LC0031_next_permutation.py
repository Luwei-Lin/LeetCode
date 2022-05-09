class Solution:
    def nextPermutation(self,nums):
        if len(nums) <= 1:
            return
        # traverse from right to find a[i - 1], which is the first element decresing
        r = len(nums) - 1 # right 
        i = r          # a[i - 1]
        ascending = True
        while i >= 1 :
            if nums[i - 1] < nums[i]:
                ascending = False
                break
            i -= 1

        found = False
        #find the min num from i to end;
        for j in range(len(nums) - 1 , i - 1, - 1):
            if nums[j] > nums[i - 1]:
                found = True #found the rest of subarray has the element bigger than a[i - 1]
                break
        #swap
        if found and not ascending:
            
            nums[j], nums[i - 1] = nums[i - 1], nums[j]
            #reverse
            l = i
            r = len(nums) - 1
            while (l < r):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        else:
            nums.reverse()
        

    def method2(self, nums):
        i = len(nums) - 1
        k = i
        while (i > 0 and nums[i-1] >= nums[i]):
            i -= 1

        j = i 
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j += 1
            k -= 1#move the middle position of subarray

        if (i > 0) :
            k = i - 1
            while (nums[k] <= nums[i]):
                k += 1# find the subarray least one bigger than i
            nums[i], nums[k] = nums[k], nums[i]


def main():
    nums = [1,5,8,4,7,6,5,3,1]
    #nums = [1, 2, 3]
    #Solution().nextPermutation(nums)
    Solution().method2(nums)
    print(nums)
main()