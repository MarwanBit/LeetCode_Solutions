class Solution:
    def minDistanceHelper(self, word1: str, word2: str) -> int:
        #Base cases for edit distance
        if word1 == "" and word2 == "":
            return 0 
        elif word1 == "" and word2 != "":
            return len(word2)
        elif word1 != "" and word2 == "":
            return len(word1)
        else:
            delete_first = 1 + self.minDistanceHelper(word1[1:], word2)
            delete_second = 1 + self.minDistanceHelper(word1, word2[1:])
            replace = 1 + self.minDistanceHelper(word1[1:], word2[1:]) 
            #if there is a match 
            if word1[0] == word2[0]:
                match = 0 + self.minDistanceHelper(word1[1:], word2[1:])
                return min(match, delete_first, delete_second, replace)
            return min(delete_first, delete_second, replace)
            
            
       
    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistanceHelper(word1, word2)

    def minDistanceDP(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]* (n + 1) for _ in range(m + 1)]
        for i in range(n + 1):
            dp[m][i] = len(word2[i:])
        for j in range(m + 1):
            dp[j][n] = len(word1[j:])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                delete_first = 1 + dp[i + 1][j]
                delete_second = 1 + dp[i][j + 1]
                replace = 1 + dp[i + 1][j + 1]
                dp[i][j] = min(delete_first, delete_second, replace)
                if word1[i] == word2[j]:
                    match = dp[i + 1][j + 1]
                    dp[i][j] = min(match, replace, delete_first, delete_second)
        return dp[0][0]