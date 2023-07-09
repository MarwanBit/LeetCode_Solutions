class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int], list[int]]:
        '''
        '''
        s1 = set(nums1)
        s2 = set(nums2)
        return [s1 - s2 , s2 - s1]
    
    def elementsOnlyInFirstList(self, nums1: list[int], nums2: list[int]) -> list[int]:
        '''
        '''
        only_in_nums1 = {}
        exists_in_nums2 = {}
        #This should be O(m) where m is the size of num_2
        for num in nums2:
            # O(1) operation, shout out to the hash tables!
            if num not in exists_in_nums2:
                exists_in_nums2[num] = 1
        # Now lets find the elements in nums1 which aren't in nums2
        for num in nums1:
            if num not in exists_in_nums2:
                only_in_nums1[num] = 1
        #Now return this set
        return list(only_in_nums1.keys())
    
        
    def findDifferenceHashMap(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        '''
        '''
        list1 = self.elementsOnlyInFirstList(nums1, nums2)
        list2 = self.elementsOnlyInFirstList(nums2, nums1)
        return [list1, list2]
    

