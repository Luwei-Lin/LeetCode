def test2():
    nums = [1, 3, 2, 4, 5]
    newNums = nums.copy()
    nums.sort()
    seenL = False
    seenR = False
    ok = True
    start = 0
    end = 0
    l = 0
    r = len(nums) - 1
    if l == r:
        return 0
    for i in range(len(nums)):
        if nums[i] != newNums[i]:
            ok = False
            break
    
    if ok:
        return 0
        
    while ok == False and l < r:
        if seenL and seenR:
            break
        if nums[l] != newNums[l] and seenL == False:
            seenL = True
            start = l
        if nums[r] != newNums[r] and seenR == False:
            seenR = True
            end = r
        if nums[l] == newNums[l]:
            l += 1
        if nums[r] == newNums[r]:
            r -= 1
        
        
        
    print(end - start + 1)
    
    print(nums)
    print(newNums)

def main():
    test2()

main()