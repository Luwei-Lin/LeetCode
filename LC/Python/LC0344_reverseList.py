class Solution:
    def reverseString(self, s):
        s.reverse()
    def reverseString2(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
            
def main():
    s = ["h","e","l","l","o"]
    Solution().reverseString2(s)
    print(s)

main()
