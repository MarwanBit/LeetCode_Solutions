class Solution:
    def MergeAlternatively(self, word1: str, word2: str) -> str:

        #init vars
        n = max(len(word1), len(word2))
        word = []

        #Now lets loop through
        for index in range(n):
            if index < len(word1):
                word.append(word1[index])
            if index < len(word2):
                word.append(word2[index])
        
        return "".join(word)