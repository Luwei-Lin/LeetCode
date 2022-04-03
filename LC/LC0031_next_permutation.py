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
            temp = nums[j]
            nums[j] = nums[i - 1]
            nums[i - 1] = temp
        
            #reverse
            
            l = i
            r = len(nums) - 1
            while (l < r):
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
                r -= 1
        else:
            nums.reverse()
def main():
    nums = [1,5,8,4,7,6,5,3,1]
    #nums = [1, 2, 3]
    Solution().nextPermutation(nums)
    print(nums)
main()