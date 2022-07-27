class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        assert (len(s))> 0
        res = d.get(s[0])
        for i in range(1, len(s)):
            curr_c = d.get(s[i])
            prev_c = d.get(s[i - 1])
            
            if curr_c > prev_c:
                res += curr_c - 2 * prev_c
            else:
                res += curr_c
        return res  
def main():
    s = Solution()
    print(s.romanToInt("MCMXCIV"))
    #print(s.romanToInt("IV"))
main()