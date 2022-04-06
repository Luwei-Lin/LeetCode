class Solution:
    def countBits(self, n):
        res = []
        for i in range(0, n + 1):
            count = 0
            while (i):
                if (i & 1):
                    count += 1
                i = i >> 1
            res.append(count)
        return res
    # Most signifigant bit DP
    # dp: P(x + b) = P(x) + 1 b = 2^m > x  
    def countBits_dp1(self, n):
        res = [0] * (n + 1)
        x = 0
        b = 1
        while b <= n:
            while b > x and x + b <= n:
                res[x + b] = res[x] + 1 
                x += 1
            b <<= 1 # b = 2b
            x = 0
        return res
        
    #dp: P(x) = P(x // 2) + (x % 2)
    def countBits_dp2(self, n):
        res = [0] * (n + 1)
        for i in range (1, n + 1):
            res[i] = res[i >> 1] + (i & 1) # dp to find res [i / 2] and (i & 1);
            # res [101] = res[10] + (101 & 001)
        return res
    
    #dp: P(x) = P(x & (x - 1)) + 1
    def countBits_dp3(self, n):
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i & (i - 1)] + 1
        return res

def main():
    n = 5
    print(Solution().countBits_dp1(n))

main()