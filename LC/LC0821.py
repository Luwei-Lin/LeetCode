
class Solution:
    def shortestToChar(self, s: str, c: str):
        res = []
        pos = -len(s)
        for i in range(len(s)):
            if s[i] == c:
                pos = i
            res.append(i - pos) 
        for i in range(pos - 1, -1, -1):
            if s[i] == c:
                pos = i
            res[i] = min(res[i], pos - i)
        return res
def main():
    #s = "loveleetcode"
    s = "aaba"
    c = "b"
    print(Solution().shortestToChar(s, c))

main()
