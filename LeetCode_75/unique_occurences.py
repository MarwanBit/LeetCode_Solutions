class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        '''
        '''
        nums_frq: dict = {}
        #fill nums_frequency hashmap
        for num in arr:
            if num not in nums_frq:
                nums_frq[num] = 1 
            else:
                nums_frq[num] += 1 
        #Now we must iterate through the frequencies list
        frq_list = nums_frq.values()
        frq_dict: dict = {}
        for frq in frq_list:
            if frq not in frq_dict:
                frq_dict[frq] = 1
            else:
                return False
        return True
    
    def uniqueOccurrencesAlt(self, arr: list[int]) -> bool:
        '''
        '''
        nums_frq: dict = {}
        #fill nums_frequency hashmap
        for num in arr:
            if num not in nums_frq:
                nums_frq[num] = 1 
            else:
                nums_frq[num] += 1 
        #Now we must iterate through the frequencies list
        frq_list = nums_frq.values()
        if len(frq_list) == len(set(frq_list)):
            return True
        return False