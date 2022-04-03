class Solution:
    def is_parlidrome(self, l, r, sub_s):
        left = 0
        right = len(sub_s) - 1
        while (left < right):
            if sub_s[left] != sub_s[right]:
                return False
            left += 1
            right -= 1
        return True
    def verison1(self, s):
        s = list(s)
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                break
            l += 1
            r -= 1
        if (l >= r):
            return True
        elif self.is_parlidrome(l + 1, r, s[l + 1 : r + 1]) or self.is_parlidrome(l, r - 1, s[l: r]):
            return True
        return False  

    def version2(self, s):
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                one = s[left:right]
                two = s[left+1:right+1]
                return one == one[::-1] or two == two[::-1]
            left += 1
            right -= 1   
def main():
    s = "abc"
    print(Solution().verison1(s))
main()