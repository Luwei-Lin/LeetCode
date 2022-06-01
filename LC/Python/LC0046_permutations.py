from doctest import FAIL_FAST


def test():
    nums = [1, 1, 3]
    ans = []
    used = [False for i in range( 0 , len(nums))]
    
    t = []
    
    def backtrack (nums, temp, used):
        if len(temp) == len(nums):
            #need to creat new temp list otherwisse the the temp will modify itself
            newTemp = temp.copy()
            ans.append(newTemp)
            return
        for i in range (0, len(nums)):
            if used [i]:
                continue

            temp.append(nums[i])
            used[i] = True
            
            backtrack(nums, temp, used)
            
            temp.pop()
            used[i] = False
            
    backtrack(nums, t, used)
    print(ans)
test()
