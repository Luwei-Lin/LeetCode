from curses.ascii import NUL
from operator import truediv


def test():
    
    nums = [1, 2, 3, 4, 5, 0]
    #nums.sort() #[1, 3, 3, 3, 4]
    k = 6
    count = 0
    found = False
    for i in range(len(nums)):
        if nums[i] == 0: continue
        for j in range (i + 1, len(nums)):
            if nums[j] == 0: continue
            if nums[i] + nums[j] == k:
                nums[i] = nums[j] = 0
                count += 1
                break
    
            
            
    print(count)

def test2():
    nums = [1, 3, 4, 5]
    #nums.sort() #[1, 3, 3, 3, 4]
    k = 5
    d = {}
    count = 0
    for n in nums:
        if d.get(n) == None:
            d[n] = 1
        else :
            d[n] += 1
    print (d)
    for n in nums:
        cur = n
        complement = k - cur
        if d.get(cur) != None and d.get(complement) != None:
            if cur == complement and d[cur] - 1 > 0:
                count += 1
                d[cur] -= 2
            elif cur != complement and d[cur] > 0 and d[complement] > 0:
                count += 1
                d[cur] -= 1
                d[complement] -= 1
    print(count)
def main():
    test2()
main()