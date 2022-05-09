def test1():
    nums1 = [3,1,2]
    nums2 = [1,1]
    ans = []
    table = {}
    temp = []
    if len(nums1) < len(nums2):
        temp = nums1
        nums1 = nums2
        nums2 = temp
    print(nums1)
    print(nums2)
    p = 0
    for n in nums1:
        if n in table.keys():
            table[n] += 1
        else:
            table[n] = 1
    print(table)
    for e in nums2:
        
        if e in table.keys() and table.get(e, 0) > 0:
            
            table[e] -= 1
            nums2[p] = e
            p += 1
    print(nums2)
test1()