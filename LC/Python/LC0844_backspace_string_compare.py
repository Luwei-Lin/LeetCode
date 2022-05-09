class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        vs = []
        vt = []
        #check the '#'
        for c in s:
            if c != '#' :
                vs.append(c)
            elif (c == '#' and len(vs) != 0):
                vs.pop()
            else:
                continue
        for c in t:
            if c != '#' :
                vt.append(c)
            elif (c == '#' and len(vt) != 0):
                vt.pop()
            else:
                continue
                
        vs_l = len(vs)
        vt_l = len(vt)
        if (vs_l != vt_l):
            return False
        else:
            for i in range(vs_l):
                if vs[i] != vt[i]:
                    return False
        return True
        
def main():
    s = "a##c"
    t = "#a#c"
    
    print(Solution().backspaceCompare(s, t))
main()