class Solution:
    def constructFreqDict(self, word1: str) -> dict:
        '''
        '''
        freq_dict1 = {}
        for char in word1: 
            if char not in freq_dict1:
                freq_dict1[char] = 1
            else: 
                freq_dict1[char] += 1 
        return freq_dict1

    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        '''
        set1 = set(word1)
        set2 = set(word2)
        #First check if the sets are equal
        if set1 != set2: 
            return False
        #now the idea is we want to check if the {char: freq} dictionaries 
        # for each of the sets are equal so lets product these
        freq_dict1 = self.constructFreqDict(word1)
        freq_dict2 = self.constructFreqDict(word2)
        freq_list1 = freq_dict1.values()
        freq_list2 = freq_dict2.values()
        freq_freq_list1 = self.constructFreqDict(freq_list1)
        freq_freq_list2 = self.constructFreqDict(freq_list2)
        return freq_freq_list1 == freq_freq_list2
    

    
    def closeStringsOpt(self, word1: str, word2: str) -> bool:
        '''
        '''
        set1 = set(word1)
        set2 = set(word2)
        #First check if the sets are equal
        if set1 != set2: 
            return False
        #now the idea is we want to check if the {char: freq} dictionaries 
        # for each of the sets are equal so lets product these
        freq_dict1 = self.constructFreqDict(word1)
        freq_dict2 = self.constructFreqDict(word2)
        freq_list1 = list(freq_dict1.values())
        freq_list2 = list(freq_dict2.values())
        freq_list1.sort()
        freq_list2.sort()
        return freq_list1 == freq_list2

if __name__ == "__main__":
    sol = Solution()
    print(sol.closeStrings("abc", "bca"))