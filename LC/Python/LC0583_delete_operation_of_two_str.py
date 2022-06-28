
class Solution:
    def longestCommonSubsequence(self, word1:str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[l1][l2]
        
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        lcs = self.longestCommonSubsequence(word1, word2)
        return l1 + l2 - 2 * lcs
def main():
    s = Solution()
    print(s.minDistance("sea", "eat"))
    print(s.minDistance("leetcode", "etco"))

main()