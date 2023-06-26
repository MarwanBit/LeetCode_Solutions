class Solution:
    #Works but is to slow I think this is O(m^2)
    def isSubsequence(self, s: str, t: str, memo={}) -> bool:
        '''
        there are many approaches to this, we can do a memoization/ dynamic programming approach/
        recursive approach on t
`       
        let's consider this other approach though which uses sets
        '''
        #let's establish a base case
        sol_1 = False
        sol_2 = False 
        if s == "":
            return True
        elif t == "":
            return False
        #now we create the branches 
        if s[0] == t[0]:
            sol_1 = self.isSubsequence(s[1:], t[1:])
        #otherwise we try moving on
        sol_2 = self.isSubsequence(s, t[1:])

        return sol_1 or sol_2

    def isSubsequenceOptimal(self, s: str, t: str) -> bool:
        '''
        This is O(n)
        '''
        i, j = 0, 0 
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False
    

    def isSubsequenceRecursive(self, s: str, t: str) -> bool:
        '''
        '''
        i, j = 0, 0 
        #Handle the base cases
        if s == "":
            return True 
        elif t == "":
            return False
        #now we setup the recursion
        if s[i] == t[i]:
            return self.isSubsequenceRecursive(s[1:], t[1:])
        else:
            return self.isSubsequenceRecursive(s, t[1:])
        
    
    def isSubsequenceDP(self, s: str, t: str) -> bool:
        '''
        '''
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for i in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = True 
                elif j == 0:
                    dp[i][j] == False
                elif s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j-1]
        print(dp)
        return dp[m][n]

        





if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    t = "ahbgdc"
    print(sol.isSubsequenceDP(s, t))