class Solution:
    '''
    This is the niave recursive solution that works but it too slow,
    the time complexity of this should be 3^ min(n, m) which is way 
    to slow, so what we must do is memoize this using DP

    We can do this by creating the table that is m*n, where m is the length
    of text1 and n is the length of text2
    '''
    def lcs_helper(self, i, j, text1: str, text2: str) -> int:
        if text1[i:] == "" or text2[j:] == "":
            return 0 
        else:
            use_first = self.lcs_helper(i + 1, j, text1, text2)
            use_second = self.lcs_helper(i, j + 1, text1, text2)
            use_both = (text1[i] == text2[j]) + self.lcs_helper(i + 1, j + 1, text1, text2)
            return max(use_both, use_first, use_second)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.lcs_helper(0, 0, text1, text2)


    def longestCommonSubsequenceDP(self, text1: str, text2: str) -> int:
        m, n = len(text1) + 1, len(text2) + 1
        dp = [[0] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                use_first = dp[i - 1][j]
                use_second = dp[i][j - 1]
                use_both = (text1[i - 1] == text2[j - 1]) + dp[i - 1][j - 1]
                dp[i][j] = max(use_first, use_second, use_both)
        return dp[m - 1][n - 1]
