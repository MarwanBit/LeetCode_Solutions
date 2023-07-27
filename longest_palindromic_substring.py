class Solution():
    def longestPalindrome(self, s: str) -> str:
        '''
        The idea of this approach is to use dynamic programming , let's consider this
        '''
        max_palindrome_len = 0 
        max_palindrome_indices = (0,0)
        n = len(s)
        dp = [[None]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][j] = True
                elif j < i:
                    dp[i][j] = True
        #Now we will it up for the other cases, we must build up from len 2, ... len n palindromic strings, that is why 
        #this doesn't work becauser when it encounters the final one, it looks back and finds none, we must 
        # build up the DP table in relevant way such that all the subcases are present
        for i in range(n):
            for j in range(n):
                if dp[i][j] == None:
                    if (s[i] == s[j]) and (dp[i + 1][j - 1]):
                        dp[i][j] = True 
                    elif (s[i] != s[j]) or (not dp[i+1][j-1]):
                        dp[i][j] = False
        #Now are going through and finding the longest palindromic string
        for i in range(n):
            for j in range(n):
                if dp[i][j] and len(s[i: j + 1]) >= max_palindrome_len:
                    max_palindrome_len = len(s[i: j + 1])
                    max_palindrome_indices = (i, j)
        print(dp)
        print(max_palindrome_indices, max_palindrome_len)
        return s[max_palindrome_indices[0]: max_palindrome_indices[1] + 1]
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("aba"))
    print(sol.longestPalindrome("aaaa"))